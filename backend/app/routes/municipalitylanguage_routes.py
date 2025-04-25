from fastapi import APIRouter
from app.models import MunicipalityLanguage
from app.services import municipality_language_service as mls

router = APIRouter()

@router.get("/municipalitylanguages", response_model=list[MunicipalityLanguage])
def read_municipality_languages():
    return mls.get_all_municipality_languages()

@router.post("/municipalitylanguages")
def add_municipality_language(m: MunicipalityLanguage):
    return mls.create_municipality_language(m)