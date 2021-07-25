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


# Test for successful response for year data.
def test_get_year_200():
    response = client.get('/api/academics/year/4')
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


# Test for invalid year response for year data.
def test_get_year_400():
    response = client.get('/api/academics/year/5')
    assert response.status_code == 400
    assert response.json() == {'detail': {'ERROR': 'Invalid Year', 'MESSAGE': 'Use 2, 3 or 4'}}


# Test for successful response for get subjects.
def test_get_subjects_200():
    response = client.get('/api/academics/subjects?semester=3')
    assert response.status_code == 200
    assert response.json() == [
        {
            'key': 'CS211',
            'name': 'Discrete Mathematical Structure',
            'abbreviation': 'DMS'
        },
        {
            'key': 'CS212',
            'name': 'Digital System and Microprocessor',
            'abbreviation': 'DSM'
        },
        {
            'key': 'CS213',
            'name': 'Data Structures with C',
            'abbreviation': 'DS'
        },
        {
            'key': 'CS214',
            'name': 'Data Communication',
            'abbreviation': 'DC'
        }
    ]


# Test for invalid semester response for get subjects.
def test_get_subjects_400():
    response = client.get('/api/academics/subjects?semester=1')
    assert response.status_code == 400
    assert response.json() == {'detail': {'ERROR': 'Invalid semester.'}}
