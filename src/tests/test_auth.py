"""Tests of Auth API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi.testclient import TestClient

# Own Imports
from src.main import app

client = TestClient(app)


# Test for successful response for create user
def test_create_user_201():
    response = client.post('/auth/create', json={
        "first_name": "Foo",
        "last_name": "Bar",
        "email": "foo.bar@example.com",
        "password": "changeme"
    })
    assert response.status_code == 201
    assert response.json() == {
        "first_name": "Foo",
        "last_name": "Bar",
        "email": "foo.bar@example.com",
    }


# Test for conflict response for create user
def test_create_user_409():
    response = client.post('/auth/create', json={
        "first_name": "Foo",
        "last_name": "Bar",
        "email": "foo.bar@example.com",
        "password": "changeme"
    })
    assert response.status_code == 409
    assert response.json() == {'detail': {'ERROR': 'User already exists.'}}
