from dotenv import load_dotenv
import os
import cx_Oracle

# Load environment variables from .env
load_dotenv()

def get_connection():
    try:
        connection = cx_Oracle.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Database connection error:", e)
        return None
