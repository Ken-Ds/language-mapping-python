# app/routes/phrase_routes.py
from fastapi import APIRouter, HTTPException
from app.models import Phrase
from app.db import get_connection

router = APIRouter()

@router.get("/phrases", response_model=list[Phrase])
def get_phrases():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM phrases")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@router.post("/phrases")
def create_phrase(phrase: Phrase):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO phrases (PHRASE_ID, CONTENT, LANGUAGE_ID) VALUES (%s, %s, %s)", 
                   (phrase.PHRASE_ID, phrase.CONTENT, phrase.LANGUAGE_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Phrase added successfully"}

@router.put("/phrases/{phrase_id}")
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

@router.delete("/phrases/{phrase_id}")
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
