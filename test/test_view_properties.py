from http import HTTPStatus

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_properties():
    response = client.get("/properties")
    assert response.status_code == HTTPStatus.OK
    response_value = response.json()
    assert len(response_value['data'])==55

def test_filter_properties():
    data = {"data":
           [{"other":"","dataFilter":["city","=","bogota"]}]}  
    response = client.post("/filter_properties", json=data,)
    assert response.status_code == HTTPStatus.OK
    response_value = response.json()
    assert len(response_value['data'])==8  

def test_filter_properties_starts():
    data = {"data": [{"other": "", "dataFilter": ["city", "startswith", "b"]}]}
    response = client.post("/filter_properties", json=data,)
    assert response.status_code == HTTPStatus.OK
    response_value = response.json()
    assert len(response_value['data'])==15

def test_filter_properties_endWith():
    data = {"data": [{"other": "", "dataFilter": ["city", "endswith", "n"]}]}
    response = client.post("/filter_properties", json=data,)
    assert response.status_code == HTTPStatus.OK
    response_value = response.json()
    assert len(response_value['data'])==5
    
