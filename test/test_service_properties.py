import json
from http import HTTPStatus

from app.utils.entities.entitity_propertie import PropiertierFilter, FilterModel
from app.services.propierty import get_propertie, get_filter_propertie 

def test_properties():
    response = get_propertie()
    assert response.status == HTTPStatus.OK
    assert len(response.data)==55

def test_filter_properties():
    propiertiFilter = PropiertierFilter(dataFilter=["city","=","bogota"],
    other="")
    data = FilterModel(data=[propiertiFilter])
    response = get_filter_propertie(data)
    assert response.status == HTTPStatus.OK
    assert len(response.data)==8          
    
