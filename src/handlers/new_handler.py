from data.db import get_connection
from src.utils import rows_to_dict


def media_consegne():
    conn = get_connection()
    puntatore = conn.cursor()
    puntatore.execute("select avg(consegne), nome from riders")
    conn.commit()
    risultati = puntatore.fetchall()
    return rows_to_dict(risultati)