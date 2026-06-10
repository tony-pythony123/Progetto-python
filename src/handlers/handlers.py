from data.db import get_connection
from src.utils import rows_to_dict


def get_riders():
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
            cur.execute("SELECT * FROM riders;")
            rows = cur.fetchall()
            return rows_to_dict(cur, rows)
        except Exception as e:
            print("Error in get_riders:", e)
            return None
        finally:
            cur.close()
    except Exception as e:
        print("Connection error in get_riders:", e)
        return None
    finally:
        conn.close()


def get_riders_by_vehicle(vehicle):
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
            cur.execute(
                "SELECT * FROM riders WHERE vehicle = %s;",
                (vehicle,)
            )
            rows = cur.fetchall()
            return rows_to_dict(cur, rows)
        except Exception as e:
            print("Error in get_riders_by_vehicle:", e)
            return None
        finally:
            cur.close()
    except Exception as e:
        print("Connection error in get_riders_by_vehicle:", e)
        return None
    finally:
        conn.close()


def create_review(id, rider_id, customer_name, rating, comment):
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
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
        except Exception as e:
            print("Error in create_review:", e)
            conn.rollback()
            return None
        finally:
            cur.close()
    except Exception as e:
        print("Connection error in create_review:", e)
        return None
    finally:
        conn.close()


def update_review_comment(id, comment):
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
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
        except Exception as e:
            print("Error in update_review_comment:", e)
            conn.rollback()
            return None
        finally:
            cur.close()
    except Exception as e:
        print("Connection error in update_review_comment:", e)
        return None
    finally:
        conn.close()

def remove_rider(id):
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
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
        except Exception as e:
            print("Error in remove_rider:", e)
            conn.rollback()
            return None
        finally:
            cur.close()
    except Exception as e:
        print("Connection error in remove_rider:", e)
        return None
    finally:
        conn.close()

def average_rating():
    conn = get_connection()
    try:
        cur = conn.cursor()
        try:
            cur.execute("""
                SELECT D.name, R.rider_id, ROUND(AVG(R.rating)::numeric, 2) AS avg_rating
                FROM reviews AS R
                JOIN riders AS D ON R.rider_id = D.id
                GROUP BY D.name, R.rider_id
            """)

            rows = cur.fetchall()

            print("DEBUG ROWS:", rows)
            print("DEBUG TYPES:", [type(r) for r in rows])

            return rows_to_dict(cur, rows)
        except Exception as e:
            print("Error in average_rating:", e)
            return None
        finally:
            cur.close()
    except Exception as e:
        print("Connection error in average_rating:", e)
        return None
    finally:
        conn.close()