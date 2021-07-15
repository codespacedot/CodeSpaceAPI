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
from src.settings import TestUser

client = TestClient(app)
access_token = ''


# Test for successful response for create user
def test_create_user_201():
    response = client.post('/users/create', json={
        'first_name': TestUser.F_NAME,
        'last_name': TestUser.L_NAME,
        'email': TestUser.EMAIL,
        'dob': TestUser.DOB,
        'password': TestUser.PASSWORD
    })
    assert response.status_code == 201
    assert response.json() == {'detail': 'User created.'}


# Test for conflict response for create user
def test_create_user_409():
    response = client.post('/users/create', json={
        'first_name': TestUser.F_NAME,
        'last_name': TestUser.L_NAME,
        'email': TestUser.EMAIL,
        'dob': TestUser.DOB,
        'password': TestUser.PASSWORD
    })
    assert response.status_code == 409
    assert response.json() == {'detail': {'ERROR': 'User already exists.'}}


# Test for successful response for user login
def test_login_user_200():
    global access_token
    response = client.post('/users/login', data={
        'username': TestUser.EMAIL,
        'password': TestUser.PASSWORD
    })
    assert response.status_code == 200
    assert 'access_token' in response.json()
    access_token = response.json()['access_token']


# Test for invalid response for user login
def test_login_user_400():
    response = client.post('/users/login', data={
        'username': 'foo.bar@example.com',
        'password': 'pass1234'
    })
    assert response.status_code == 400
    assert response.json() == {'detail': {'ERROR': 'Invalid credentials.'}}


# Test for successful response for change password
def test_change_password_200():
    response = client.put('/users/password/change', json={'new_password': 'pass1234'},
                          headers={'Authorization': f'Bearer {access_token}'})
    # assert response.status_code == 200
    assert response.json() == {'detail': 'Password updated.'}


# Test for successful response for delete user
def test_delete_user_200():
    response = client.delete('/users/delete', headers={
        'Authorization': f'Bearer {access_token}'
    })
    assert response.status_code == 200
    assert response.json() == {'detail': 'User deleted.'}


# Test for not authenticated response for delete user
def test_delete_user_401():
    response = client.delete('/users/delete')
    assert response.status_code == 401
    assert response.json() == {'detail': 'Not authenticated'}
