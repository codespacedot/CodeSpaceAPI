"""Router for Auth API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import APIRouter, status

# Own Imports
from . import main, models


auth_router = APIRouter(prefix='/auth', tags=['Authentication'])


@auth_router.post('/create', response_model=models.UserBase, status_code=status.HTTP_201_CREATED)
def create_user(request: models.UserIn):
    """Create new user."""
    return main.create_user(request)
