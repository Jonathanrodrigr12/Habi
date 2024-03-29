from fastapi import APIRouter
from app.core.core import cur
from app.services.propierty import get_propertie, get_filter_propertie
from app.utils.entities.entitity_propertie import ResponseModel, FilterModel

router = APIRouter()


@router.get("/properties", tags=["Propierties"], response_model=ResponseModel)
def get_properties():
    result = get_propertie()
    return result

@router.post("/filter_properties", tags=["Propierties"], response_model=ResponseModel)
def get_filter_properties(data: FilterModel):
    result = get_filter_propertie(data)
    return result
