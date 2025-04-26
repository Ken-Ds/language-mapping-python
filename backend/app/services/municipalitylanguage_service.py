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

def get_top3_dialects_by_municipality(municipality_id: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
        SELECT d.DIALECT_ID, d.DIALECT_NAME, COUNT(*) AS usage_count
        FROM municipalitylanguages ml
        JOIN dialects d ON ml.DIALECT_ID = d.DIALECT_ID
        WHERE ml.MUNICIPALITY_ID = %s
        GROUP BY d.DIALECT_ID
        ORDER BY usage_count DESC
        LIMIT 3
    """
    cursor.execute(query, (municipality_id,))
    results = cursor.fetchall()
    cursor.close()
    conn.close()

    if not results:
        raise HTTPException(status_code=404, detail="No dialects found for this municipality")
    
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