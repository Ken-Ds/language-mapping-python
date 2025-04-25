# app/routes/dialect_routes.py
from fastapi import APIRouter
from app.models import Dialect
from app.services import dialect_service as ds

router = APIRouter()

@router.get("/dialects", response_model=list[Dialect])
def read_dialects():
    return ds.get_all_dialects()

@router.post("/dialects")
def add_dialect(dialect: Dialect):
    return ds.create_dialect(dialect)

@router.put("/dialects/{dialect_id}")
def modify_dialect(dialect_id: str, dialect: Dialect):
    return ds.update_dialect(dialect_id, dialect)

@router.delete("/dialects/{dialect_id}")
def remove_dialect(dialect_id: str):
    return ds.delete_dialect(dialect_id)
