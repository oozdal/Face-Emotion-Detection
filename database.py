# database.py
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os, json

load_dotenv()

# Configure the connection to your Postgres database
def get_db_connection():
    conn = psycopg2.connect(
        os.getenv('CONNECTION_URL')
    )
    return conn

# Function to save prediction results to the database
def save_prediction_to_db(dominant_emotion, probabilities, feedback=None):
    try:
        conn = get_db_connection()
        with conn:
            with conn.cursor() as cur:

                # Get the current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

                # Convert probabilities to JSON string
                probabilities_json = json.dumps(probabilities)

                if not feedback:
                    # Insert query to insert a new prediction
                    cur.execute("""
                        INSERT INTO predictions (dominant_emotion, timestamp, probabilities)
                        VALUES (%s, %s, %s::jsonb)
                    """, (dominant_emotion, timestamp, probabilities_json))

                else:
                    # Convert feedback to JSON string
                    feedback_json = json.dumps(feedback)

                    # Select query to update the feedback
                    select_query = f"""
                        SELECT MAX(id)
                        FROM predictions
                        WHERE dominant_emotion = %s AND probabilities::jsonb = %s;
                    """

                    # Execute the SELECT statement
                    cur.execute(select_query, (dominant_emotion, probabilities_json))

                    # Fetch the result
                    rowid = cur.fetchone()[0]

                    # Update the entry with the feedback
                    cur.execute("""
                        UPDATE predictions
                        SET feedback = %s::jsonb
                        WHERE id = %s
                    """, (feedback_json, rowid))

        # Commit the transaction if everything went well
        conn.commit()
    except psycopg2.Error as e:
        print(f"Database error occurred: {e}")
    finally:
        if conn:
            conn.close()