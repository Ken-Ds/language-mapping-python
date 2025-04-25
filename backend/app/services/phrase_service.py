from fastapi import HTTPException
from app.db import get_connection
from app.models import Phrase

def get_all_phrases():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM phrases")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def create_phrase(p: Phrase):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO phrases (PHRASE_ID, CONTENT, LANGUAGE_ID) VALUES (%s, %s, %s)",
                   (p.PHRASE_ID, p.CONTENT, p.LANGUAGE_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Phrase added successfully"}

def update_phrase(phrase_id: str, p: Phrase):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE phrases SET CONTENT = %s, LANGUAGE_ID = %s WHERE PHRASE_ID = %s",
                   (p.CONTENT, p.LANGUAGE_ID, phrase_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Phrase not found")
    cursor.close()
    conn.close()
    return {"message": "Phrase updated successfully"}

def delete_phrase(phrase_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM phrases WHERE PHRASE_ID = %s", (phrase_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Phrase not found")
    cursor.close()
    conn.close()
    return {"message": "Phrase deleted successfully"}
