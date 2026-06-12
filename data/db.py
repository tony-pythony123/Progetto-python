import psycopg2
import os

def get_connection():
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    if not user or not password:
        raise ValueError("Credenziali database non configurate correttamente")

    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        dbname=os.getenv("DB_NAME", "db_gestione-consegne"),
        user=user,
        password=password,
        port=os.getenv("DB_PORT", 8082)
    )