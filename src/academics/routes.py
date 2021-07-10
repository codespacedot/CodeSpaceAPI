"""Router for Academics API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import APIRouter, status

# Own Imports
from . import main, models


academic_router = APIRouter(prefix='/academics', tags=['Academics'])


@academic_router.get('/year/{year}', response_model=models.Year, status_code=status.HTTP_200_OK)
async def data_for_year(year: int):
    """Get subjects and labs for specified academic year.

    YEAR = [2, 3, 4]
    ----
    """
    return main.get_data_for_year(year)
