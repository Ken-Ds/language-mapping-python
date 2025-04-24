# app/routes/municipality_routes.py
from fastapi import APIRouter, HTTPException
from app.models import Municipality
from app.db import get_connection

router = APIRouter()

@router.get("/municipalities", response_model=list[Municipality])
def get_municipalities():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM municipalities")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@router.post("/municipalities")
def create_municipality(m: Municipality):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO municipalities (MUNICIPALITY_ID, NAME, INFORMATION, PROVINCE_ID) VALUES (%s, %s, %s, %s)", 
                   (m.MUNICIPALITY_ID, m.NAME, m.INFORMATION, m.PROVINCE_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Municipality added successfully"}

@router.put("/municipalities/{municipality_id}")
def update_municipality(municipality_id: str, m: Municipality):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE municipalities SET NAME = %s, INFORMATION = %s, PROVINCE_ID = %s WHERE MUNICIPALITY_ID = %s",
                   (m.NAME, m.INFORMATION, m.PROVINCE_ID, municipality_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Municipality not found")
    cursor.close()
    conn.close()
    return {"message": "Municipality updated successfully"}

@router.delete("/municipalities/{municipality_id}")
def delete_municipality(municipality_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM municipalities WHERE MUNICIPALITY_ID = %s", (municipality_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Municipality not found")
    cursor.close()
    conn.close()
    return {"message": "Municipality deleted successfully"}