# database.py
import psycopg2
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

# Configure the connection to your Postgres database
def get_db_connection():
    conn = psycopg2.connect(
        os.getenv('CONNECTION_URL')
    )
    return conn

# Function to save prediction results to the database
def save_prediction_to_db(dominant_emotion):
    conn = get_db_connection()
    cur = conn.cursor()

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")

    cur.execute("""
        INSERT INTO predictions (dominant_emotion, timestamp)
        VALUES (%s, %s)
    """, (dominant_emotion, timestamp))
    
    conn.commit()
    cur.close()
    conn.close()

