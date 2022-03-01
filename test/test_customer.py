from http import HTTPStatus

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_customer():
    response = client.get("/customer/")
    assert response.status_code == HTTPStatus.OK
    response_value = response.json()
    assert response_value['data'][0]['name']=="Jonathan" and response_value['data'][0]['edad']==22
    
