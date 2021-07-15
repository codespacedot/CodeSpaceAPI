"""Router for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict
from fastapi import APIRouter, BackgroundTasks, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

# Own Imports
from . import main, models, oauth2

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_user(user: models.UserCreate, background_task: BackgroundTasks):
    """Create new user and send welcome email.

    DOB and PASSWORD: Should be encrypted at front end.
    ---
    """
    return main.create_user(user=user, task=background_task)


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


@user_router.put('/password/change', status_code=status.HTTP_200_OK)
async def change_password(password: models.ChangePassword, user: Dict = Depends(oauth2.get_current_user)):
    """Change password.

    Note:
    ---------
    Password encryption must be performed at front end.
    """
    return main.change_password(user=user, password=password)


@user_router.post('/password/forgot', status_code=status.HTTP_200_OK)
async def forgot_password(request: models.ForgotPassword, background_task: BackgroundTasks):
    """Email password reset verification code to user.

    Note:
    ---------
    DOB encryption must be performed at front end.
    """
    return main.forgot_password(data=request, task=background_task)


@user_router.put('/password/reset', status_code=status.HTTP_200_OK)
async def reset_password(request: models.ResetPassword):
    """Reset password if user has verification code."""
    return main.reset_password(data=request)
