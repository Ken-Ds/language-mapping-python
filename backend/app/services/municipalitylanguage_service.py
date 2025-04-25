from app.db import get_connection
from app.models import MunicipalityLanguage

def get_all_municipality_languages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM municipalitylanguages")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def create_municipality_language(m: MunicipalityLanguage):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO municipalitylanguages (MUNICIPALITY_ID, LANGUAGE_ID, DIALECT_ID) VALUES (%s, %s, %s)",
                   (m.MUNICIPALITY_ID, m.LANGUAGE_ID, m.DIALECT_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "MunicipalityLanguage added successfully"}