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

def get_language_statistics_by_province(province_id: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Query to get the total count of speakers for each language in the province
    cursor.execute("""
        SELECT l.NAME AS Language, SUM(pl.PERCENTAGE) AS Count
        FROM provincelanguages pl
        JOIN dialects d ON pl.DIALECT_ID = d.DIALECT_ID
        JOIN languages l ON d.LANGUAGE_ID = l.LANGUAGE_ID
        WHERE pl.PROVINCE_ID = %s
        GROUP BY l.NAME
        ORDER BY Count DESC
    """, (province_id,))
    language_data = cursor.fetchall()

    # Calculate the total count of all speakers
    total_count = sum(row['Count'] for row in language_data)

    # Add percentage to each language
    for row in language_data:
        row['Percentage'] = f"{(row['Count'] / total_count) * 100:.2f}%"

    cursor.close()
    conn.close()

    return language_data