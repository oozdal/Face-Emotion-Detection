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
def save_prediction_to_db(dominant_emotion, probabilities):
    conn = get_db_connection()
    cur = conn.cursor()

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    # Convert probabilities to JSON string
    probabilities_json = json.dumps(probabilities)

    cur.execute("""
        INSERT INTO predictions (dominant_emotion, timestamp, probabilities)
        VALUES (%s, %s, %s::jsonb)
    """, (dominant_emotion, timestamp, probabilities_json))

    conn.commit()
    cur.close()
    conn.close()

