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

def get_top10_dialects_by_province(province_id: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT d.DIALECT_ID, d.DIALECT_NAME, pl.PERCENTAGE
        FROM provincelanguages pl
        JOIN dialects d ON pl.DIALECT_ID = d.DIALECT_ID
        WHERE pl.PROVINCE_ID = %s
        ORDER BY pl.PERCENTAGE DESC
        LIMIT 10
    """
    cursor.execute(query, (province_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    if not results:
        raise HTTPException(status_code=404, detail="No dialects found for this province")

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
