"""Main functionalities of Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict
from fastapi import BackgroundTasks, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

# Own Imports
from . import db, models, oauth2
from .. import email
from ..utils import string_utils


# ========== User ======================================================================================================
def create_user(user: models.UserCreate, task: BackgroundTasks) -> Dict:
    """Create user.

    If User gets created, send welcome email to registered email id.

    Arguments:
    ---------
        user: UserCreate model.
        task: Background tasks for sending email.

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 409 if user exists.
        HTTPException 500 if database error.
    """
    if db.get_user_by_email(email=user.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={'ERROR': 'User already exists.'})
    if db.create_user(**user.dict()):
        email.send_welcome_email(background_tasks=task, email_to=user.email, name=user.first_name)
        return {'detail': 'User created.'}
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})


def login_user(user_data: OAuth2PasswordRequestForm) -> Dict:
    """Login.

    Arguments:
    ---------
        user_data: OAuth2PasswordRequestForm model.

    Returns:
    ---------
        JWT access token dictionary if login successful.

    Raises:
    ---------
        HTTPException 400 if invalid credentials.
    """
    user = db.get_user_by_email(email=user_data.username)
    if not user or user['password'] != user_data.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'ERROR': 'Invalid credentials.'})
    access_token = oauth2.create_access_token(data={'sub': user_data.username})
    return {'access_token': access_token, 'token_type': 'bearer'}


def delete_user(user: Dict) -> Dict:
    """Delete user.

    Arguments:
    ---------
        user: User dictionary.

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 400 if user doesn't exists.
    """
    key = user['key']
    if not db.delete_user(key=key):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'ERROR': "User doesn't exists."})
    return {'detail': 'User deleted.'}


# ========== User Profile ==============================================================================================
def get_profile(key: str) -> Dict:
    """Get User profile.

    Arguments:
    ---------
        key: User's database key.

    Returns:
    ---------
        User profile dictionary.

    Raises:
    ---------
        HTTPException 404 if user doesn't exists.
    """
    profile = db.get_profile(key=key)
    if not profile:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'ERROR': "User doesn't exists."})
    name = ''
    name += profile.pop('first_name') + ' ' + profile.pop('last_name')
    profile['name'] = name
    return profile


def get_current_profile(user: Dict) -> Dict:
    """Get logged in user's profile.

    Arguments:
    ---------
        user: User dictionary.

    Returns:
    ---------
        User profile dictionary.
    """
    return get_profile(user['key'])


def update_profile(user: Dict, updates: models.ProfileUpdate) -> Dict:
    """Update user profile.

    Arguments:
    ---------
        user: User dictionary.
        updates: Field to update.

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 500 if database error.
    """
    # Remove empty fields, so that those won't get updated
    updates = updates.dict()
    items_to_remove = []
    for item in updates:
        if not updates[item]:
            items_to_remove.append(item)

    for item in items_to_remove:
        updates.pop(item)
    # ----------------------------------------------------

    if not db.update_profile(key=user['key'], **updates):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})
    return {'detail': 'Profile updated.'}


# ========== Password ==================================================================================================
def _update_password(key: str, new_password: str) -> Dict:
    """Update password.

    Arguments:
    ---------
        key: User's database key.
        new_password: New password.

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 500 if database error.
    """
    if not db.update_password(key=key, new_password=new_password):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})
    return {'detail': 'Password updated.'}


def change_password(user: Dict, password: models.ChangePassword) -> Dict:
    """Change password of logged in user.

    Arguments:
    ---------
        user: User dictionary.
        password: New password.

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 500 if database error.
    """
    return _update_password(key=user['key'], new_password=password.new_password)


def forgot_password(data: models.ForgotPassword, task: BackgroundTasks) -> Dict:
    """Email verification code for password reset.
    If user details are matching, an email code is sent to registered email id.

    Arguments:
    ---------
        data: User details, [email, dob]
        task: Background tasks for sending email.

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 400 if invalid details.
        HTTPException 500 if database error.
    """
    user = db.get_user_by_email(email=data.email)
    if not user or user['dob'] != data.dob:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'ERROR': 'Invalid details.'})

    verification_code = string_utils.verification_code()

    if db.add_password_reset_request(key=verification_code, user_key=user['key']):
        email.send_password_verification_email(background_tasks=task, email_to=user['email'],
                                               name=user['first_name'], code=verification_code)
        return {'detail': 'Verification code sent.'}

    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail={'ERROR': 'Internal Error.'})


def reset_password(data: models.ResetPassword) -> Dict:
    """Rest password.
    Update password if verification code is matching.

    Arguments:
    ---------
        data: [new password, verification code]

    Returns:
    ---------
        Success message dictionary.

    Raises:
    ---------
        HTTPException 400 if invalid verification code.
    """
    request = db.verify_password_reset_request(key=data.verification_code)
    if not request:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={'ERROR': "Request doesn't exists."})
    return _update_password(key=request['user_key'], new_password=data.new_password)
