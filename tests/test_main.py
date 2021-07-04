from fastapi.testclient import TestClient

import api

client = TestClient(api.app)


def test_index():
    response = client.get('/api')
    assert response.status_code == 200
    assert response.json() == {'data': 'FastAPI Project'}
