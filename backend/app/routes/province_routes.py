# app/routes/province_routes.py
from fastapi import APIRouter, HTTPException
from app.models import Province
from app.db import get_connection

router = APIRouter()

@router.get("/provinces", response_model=list[Province])
def get_provinces():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM provinces")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@router.post("/provinces")
def create_province(province: Province):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO provinces (PROVINCE_ID, NAME, INFORMATION) VALUES (%s, %s, %s)", 
                   (province.PROVINCE_ID, province.NAME, province.INFORMATION))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Province added successfully"}

@router.put("/provinces/{province_id}")
def update_province(province_id: str, province: Province):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE provinces SET NAME = %s, INFORMATION = %s WHERE PROVINCE_ID = %s",
                   (province.NAME, province.INFORMATION, province_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Province not found")
    cursor.close()
    conn.close()
    return {"message": "Province updated successfully"}

@router.delete("/provinces/{province_id}")
def delete_province(province_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM provinces WHERE PROVINCE_ID = %s", (province_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Province not found")
    cursor.close()
    conn.close()
    return {"message": "Province deleted successfully"}