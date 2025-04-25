from fastapi import HTTPException
from app.db import get_connection
from app.models import Dialect

def get_all_dialects():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dialects")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def create_dialect(d: Dialect):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dialects (DIALECT_ID, DIALECT_NAME, LANGUAGE_ID) VALUES (%s, %s, %s)",
                   (d.DIALECT_ID, d.DIALECT_NAME, d.LANGUAGE_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Dialect added successfully"}

def update_dialect(dialect_id: str, d: Dialect):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE dialects SET DIALECT_NAME = %s, LANGUAGE_ID = %s WHERE DIALECT_ID = %s",
                   (d.DIALECT_NAME, d.LANGUAGE_ID, dialect_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Dialect not found")
    cursor.close()
    conn.close()
    return {"message": "Dialect updated successfully"}

def delete_dialect(dialect_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dialects WHERE DIALECT_ID = %s", (dialect_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Dialect not found")
    cursor.close()
    conn.close()
    return {"message": "Dialect deleted successfully"}