# app/services/language_service.py
from fastapi import HTTPException
from app.models import Language
from app.db import get_connection

def get_all_languages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM languages")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def create_language(language: Language):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO languages (LANGUAGE_ID, NAME) VALUES (%s, %s)",
                   (language.LANGUAGE_ID, language.NAME))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Language added successfully"}

def update_language(language_id: str, language: Language):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE languages SET NAME = %s WHERE LANGUAGE_ID = %s",
                   (language.NAME, language_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Language not found")
    cursor.close()
    conn.close()
    return {"message": "Language updated successfully"}

def delete_language(language_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM languages WHERE LANGUAGE_ID = %s", (language_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Language not found")
    cursor.close()
    conn.close()
    return {"message": "Language deleted successfully"}