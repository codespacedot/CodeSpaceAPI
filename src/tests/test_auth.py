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
    response = client.post('/users/create', json={
        'first_name': 'Foo',
        'last_name': 'Bar',
        'email': 'foo.bar@example.com',
        'password': 'password'
    })
    assert response.status_code == 201
    assert response.json() == {'detail': 'User created.'}


# Test for conflict response for create user
def test_create_user_409():
    response = client.post('/users/create', json={
        'first_name': 'Foo',
        'last_name': 'Bar',
        'email': 'foo.bar@example.com',
        'password': 'password'
    })
    assert response.status_code == 409
    assert response.json() == {'detail': {'ERROR': 'User already exists.'}}


# Test for successful response for user login
def test_login_user_200():
    response = client.post('/users/login', json={
        'username': 'foo.bar@example.com',
        'password': 'password'
    })
    assert response.status_code == 200
    assert 'access_token' in response.json()


# Test for invalid response for user login
def test_login_user_400():
    response = client.post('/users/login', data={
        'email': 'foo.bar@example.com',
        'password': 'pass1234'
    })
    assert response.status_code == 400
    assert response.json() == {'detail': {'ERROR': 'Invalid credentials.'}}


# Test for successful response for delete user
def test_delete_user_200():
    response = client.delete(f'/users/delete')
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted.'}


# Test for not found response for delete user
def test_delete_user_404():
    response = client.delete(f'/users/delete')
    assert response.status_code == 401
    assert response.json() == {'detail': {'ERROR': "User doesn't exists."}}
