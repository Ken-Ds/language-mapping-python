# app/main.py
from fastapi import FastAPI
from app.routes.language_routes import router as language_router
from app.routes.dialect_routes import router as dialect_router
from app.routes.municipality_routes import router as municipality_router
from app.routes.tourist_spot_routes import router as tourist_spot_router

app = FastAPI()

app.include_router(language_router)
app.include_router(dialect_router)
app.include_router(municipality_router)
app.include_router(tourist_spot_router)

