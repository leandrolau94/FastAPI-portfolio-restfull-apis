from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_create_patient():
    response = client.post(
        "/patients/create",
        headers={
            "Content-Type": "application/json",
        },
        json={
            "full_name": "Leandro Daniel Lau Alfonso",
            "email": "l1d9l9a4@gmail.com",
            "genre": "Male",
            "age": 28,
            "address": "Txurdinaga, Bilbao, Spain",
            "dni": "99999999R"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "full_name": "Leandro Daniel Lau Alfonso",
        "email": "l1d9l9a4@gmail.com",
        "genre": "Male",
        "age": 28,
        "address": "Txurdinaga, Bilbao, Spain",
        "dni": "99999999R",
        "anamnesis": [],
        "urgency_inform": [],
        "cronologic_evolution": [],
        "medical_orders": [],
    }