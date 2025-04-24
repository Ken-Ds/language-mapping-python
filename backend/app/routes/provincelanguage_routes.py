from fastapi import APIRouter
from app.models import ProvinceLanguage
from app.db import get_connection

router = APIRouter()

@router.get("/provincelanguages", response_model=list[ProvinceLanguage])
def get_province_languages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM provincelanguages")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@router.post("/provincelanguages")
def create_province_language(pl: ProvinceLanguage):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO provincelanguages (PROVINCE_ID, DIALECT_ID, PERCENTAGE) VALUES (%s, %s, %s)", 
                   (pl.PROVINCE_ID, pl.DIALECT_ID, pl.PERCENTAGE))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "ProvinceLanguage added successfully"}
