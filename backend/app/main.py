# app/main.py
from fastapi import FastAPI
from app.routes.language_routes import router as language_router

app = FastAPI()

app.include_router(language_router)
