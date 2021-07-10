"""Tests of Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '06/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi.testclient import TestClient

# Own Imports
from src.main import app

client = TestClient(app)


# Test for successful response for year data
def test_get_year_200():
    response = client.get('/academics/year/4')
    assert response.status_code == 200
    assert response.json()['EVEN_SEMESTER']['LABS'] == [
        {
            'abbreviation': "SC",
            'key': 'CS422L',
            'name': 'Soft Computing Lab'
        },
        {
            'abbreviation': 'WT-2',
            'key': 'CS426L',
            'name': 'Web Technology Lab'
        }
    ]


# Test for not found response for year data
def test_get_year_404():
    response = client.get('/academics/year/0')
    assert response.status_code == 404
    assert response.json() == {'detail': {'ERROR': 'Invalid Year', 'MESSAGE': 'Use 2, 3 or 4'}}
