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
    cur.execute("""
        INSERT INTO predictions (dominant_emotion)
        VALUES (%s)
    """, (dominant_emotion,))
    conn.commit()
    cur.close()
    conn.close()

