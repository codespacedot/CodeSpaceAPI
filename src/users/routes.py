"""Router for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import APIRouter, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import Dict

# Own Imports
from . import main, models, oauth2


user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user: models.UserCreate):
    """Create new user."""
    return main.create_user(user=user)


@user_router.delete('/delete', status_code=status.HTTP_200_OK)
async def delete_user(user: Dict = Depends(oauth2.get_current_user)):
    """Delete user."""
    return main.delete_user(user=user)


@user_router.post('/login', response_model=models.Token, status_code=status.HTTP_200_OK)
async def login_user(user_data: OAuth2PasswordRequestForm = Depends()):
    """Log in user.

    USERNAME = EMAIL
    ----
    """
    return main.login_user(user_data=user_data)
