from fastapi import APIRouter
from app.models import ProvinceLanguage
from app.services import provincelanguage_service as pls

router = APIRouter()

@router.get("/provincelanguages", response_model=list[ProvinceLanguage])
def read_province_languages():
    return pls.get_all_province_languages()

@router.post("/provincelanguages")
def add_province_language(p: ProvinceLanguage):
    return pls.create_province_language(p)