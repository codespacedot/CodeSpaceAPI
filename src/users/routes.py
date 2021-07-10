"""Router for Auth API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

# Own Imports
from . import main, models


user_router = APIRouter(prefix='/users', tags=['Authentication'])


@user_router.post('/create', response_model=models.UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(request: models.UserIn):
    """Create new user."""
    return main.create_user(request)


@user_router.delete('/delete/{key}', status_code=status.HTTP_200_OK)
async def delete_user(key: str):
    """Delete user."""
    return main.delete_user(key)


@user_router.post('/login', response_model=models.Token, status_code=status.HTTP_200_OK)
async def login_user(request: OAuth2PasswordRequestForm = Depends()):
    """Log in user."""
    return main.login_user(request)
