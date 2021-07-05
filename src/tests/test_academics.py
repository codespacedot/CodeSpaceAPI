from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_year_data():
    response = client.get('/academics/final-year')
    assert response.status_code == 200
    assert response.json()['EVEN_SEMESTER']['LABS'] == [
        {
            "abbreviation": "SC",
            "key": "CS422L",
            "name": "Soft Computing Lab",
            "semester": 8,
            "year": "final-year"
        },
        {
            "abbreviation": "WT-2",
            "key": "CS426L",
            "name": "Web Technology Lab",
            "semester": 8,
            "year": "final-year"
        }
    ]
