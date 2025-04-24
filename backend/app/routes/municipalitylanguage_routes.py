from fastapi import APIRouter
from app.models import MunicipalityLanguage
from app.db import get_connection

router = APIRouter()

@router.get("/municipalitylanguages", response_model=list[MunicipalityLanguage])
def get_municipality_languages():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM municipalitylanguages")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@router.post("/municipalitylanguages")
def create_municipality_language(item: MunicipalityLanguage):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO municipalitylanguages (MUNICIPALITY_ID, LANGUAGE_ID, DIALECT_ID) VALUES (%s, %s, %s)", 
                   (item.MUNICIPALITY_ID, item.LANGUAGE_ID, item.DIALECT_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "MunicipalityLanguage added successfully"}
