from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_get_year_200():
    response = client.get('/academics/4')
    assert response.status_code == 200
    assert response.json()['EVEN_SEMESTER']['LABS'] == [
        {
            "abbreviation": "SC",
            "key": "CS422L",
            "name": "Soft Computing Lab",
            "semester": 8,
            "year": 4
        },
        {
            "abbreviation": "WT-2",
            "key": "CS426L",
            "name": "Web Technology Lab",
            "semester": 8,
            "year": 4
        }
    ]


def test_get_year_404():
    response = client.get('/academics/0')
    assert response.status_code == 404
    assert response.json() == {"detail": "Invalid year"}
