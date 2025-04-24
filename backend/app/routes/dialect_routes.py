# app/routes/dialect_routes.py
from fastapi import APIRouter, HTTPException
from app.models import Dialect
from app.db import get_connection

router = APIRouter()

@router.get("/dialects", response_model=list[Dialect])
def get_dialects():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM dialects")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

@router.post("/dialects")
def create_dialect(dialect: Dialect):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dialects (DIALECT_ID, DIALECT_NAME, LANGUAGE_ID) VALUES (%s, %s, %s)", 
                   (dialect.DIALECT_ID, dialect.DIALECT_NAME, dialect.LANGUAGE_ID))
    conn.commit()
    cursor.close()
    conn.close()
    return {"message": "Dialect added successfully"}

@router.put("/dialects/{dialect_id}")
def update_dialect(dialect_id: str, dialect: Dialect):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE dialects SET DIALECT_NAME = %s, LANGUAGE_ID = %s WHERE DIALECT_ID = %s",
                   (dialect.DIALECT_NAME, dialect.LANGUAGE_ID, dialect_id))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Dialect not found")
    cursor.close()
    conn.close()
    return {"message": "Dialect updated successfully"}

@router.delete("/dialects/{dialect_id}")
def delete_dialect(dialect_id: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dialects WHERE DIALECT_ID = %s", (dialect_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Dialect not found")
    cursor.close()
    conn.close()
    return {"message": "Dialect deleted successfully"}