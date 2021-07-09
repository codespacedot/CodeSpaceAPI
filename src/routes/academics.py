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
from src.models import academics as models

router = APIRouter(prefix='/academics', tags=['Academics'])


@router.get('/year/{year}', response_model=models.Year, status_code=status.HTTP_200_OK)
def data_for_year(year: int):
    """Get subjects and labs for specified academic year.

    YEAR = [2, 3, 4]
    ----
    """
    return core.get_data_for_year(year)
