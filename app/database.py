import os
import cx_Oracle

def get_connection():
    """Establish a connection to the Oracle database."""
    try:
        connection = cx_Oracle.connect(
            user=os.getenv("DB_USER", "SYSTEM"),
            password=os.getenv("DB_PASSWORD", "241995270604"),
            dsn=os.getenv("DB_DSN", "localhost:1521/XEPDB1")
        )
        return connection
    except cx_Oracle.DatabaseError as e:
        print("Database connection error:", e)
        return None