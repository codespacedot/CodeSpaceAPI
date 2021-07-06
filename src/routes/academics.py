"""Router for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '06/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import APIRouter, status

# Own Imports
from src.core import academics as core

router = APIRouter(prefix='/academics', tags=['Academics'])


@router.get('/year/{year}', status_code=status.HTTP_200_OK)
def data_for_year(year: str):
    """Get subjects and labs for specified academic year.

    Parameters:
    ----------
        year: second / third / final

    Response:
    ----------
        {
        'ODD_SEMESTER': {
            'SUBJECTS': [],
            'LABS': []
        },
        'EVEN_SEMESTER': {
            'SUBJECTS': [],
            'LABS': []
        }
    """
    return core.get_data_for_year(year)
