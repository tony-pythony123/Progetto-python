def rows_to_dict(cursor, rows):
    columns = [desc[0] for desc in cursor.description]
    return [dict(zip(columns, row)) for row in rows]