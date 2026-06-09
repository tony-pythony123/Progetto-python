from data.db import get_connection
from src.utils import rows_to_dict
    

def get_riders():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM riders;")
        rows = cur.fetchall()
        return rows_to_dict(cur, rows)
    finally:
        cur.close()
        conn.close()


def get_reviews():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM reviews;")
        rows = cur.fetchall()
        return rows_to_dict(cur, rows)
    finally:
        cur.close()
        conn.close()