import psycopg2
import os

def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname="db_gestione-consegne",
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "Bari2025"),
        port=os.getenv("DB_PORT", 8082)
    )