from app.db import get_connection
from app.models import ProvinceLanguage

def get_all_province_languages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM provincelanguages")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def create_province_language(p: ProvinceLanguage):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO provincelanguages (PROVINCE_ID, DIALECT_ID, PERCENTAGE) VALUES (%s, %s, %s)",
                   (p.PROVINCE_ID, p.DIALECT_ID, p.PERCENTAGE))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "ProvinceLanguage added successfully"}
