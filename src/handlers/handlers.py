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

def get_riders_by_vehicle(vehicle):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM riders WHERE vehicle = %s;",
            (vehicle,)
        )
        rows = cur.fetchall()
        return rows_to_dict(cur, rows)
    finally:
        cur.close()
        conn.close()

def create_review(id, rider_id, customer_name, rating, comment):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO reviews (
                id,
                rider_id,
                customer_name,
                rating,
                comment
            )
            VALUES (%s, %s, %s, %s, %s)
            RETURNING *;
            """,
            (id, rider_id, customer_name, rating, comment)
        )
        row = cur.fetchone()
        conn.commit()
        return rows_to_dict(cur, [row])[0]
    finally:
        cur.close()
        conn.close()

def update_review_comment(id, comment):
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute(
            """
            UPDATE reviews
            SET comment = %s
            WHERE id = %s
            RETURNING *;
            """,
            (comment, id)
        )
        row = cur.fetchone()
        conn.commit()
        if row is None:
            return None
        return rows_to_dict(cur, [row])[0]
    finally:
        cur.close()
        conn.close()

def remove_rider(id):
    conn=get_connection()
    try:
        cur=conn.cursor()
        cur.execute(
            """
            DELETE FROM riders
            WHERE id = %s
            RETURNING *;
            """,
            (id,)
        )
        row = cur.fetchone()
        conn.commit()
        if row is None:
            return None
        return rows_to_dict(cur, [row])[0]
    finally:
        cur.close()
        conn.close()

def media_consegne():
    conn = get_connection()
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT D.name, R.rider_id, AVG(R.rating) AS avg_rating
            FROM reviews AS R
            JOIN riders AS D ON R.rider_id = D.id
            GROUP BY D.name, R.rider_id
        """)

        rows = cur.fetchall()

        print("DEBUG ROWS:", rows)
        print("DEBUG TYPES:", [type(r) for r in rows])

        return rows_to_dict(cur, rows)

    finally:
        cur.close()
        conn.close()