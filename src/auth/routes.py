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


@auth_router.post('/create', response_model=models.UserOut, status_code=status.HTTP_201_CREATED)
def create_user(request: models.UserIn):
    """Create new user."""
    return main.create_user(request)


@auth_router.delete('/delete/{key}', status_code=status.HTTP_200_OK)
def delete_user(key: str):
    """Delete user."""
    return main.delete_user(key)


@auth_router.post('/login', response_model=models.UserLoginOut, status_code=status.HTTP_200_OK)
def login_user(request: models.UserLoginIn):
    """Log in user."""
    return main.login_user(request)
