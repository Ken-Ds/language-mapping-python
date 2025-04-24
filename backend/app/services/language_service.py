# app/services/language_service.py

from app.database import get_connection

def get_all_languages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM languages")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
