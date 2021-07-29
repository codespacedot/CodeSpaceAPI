"""Database operations for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict, Optional

# Own Imports
from src.settings import BASE_USER, BASE_PROFILE, BASE_PASSWORD_RESET


# ========== User ======================================================================================================
def create_user(first_name: str, last_name: str, email: str, password: str) -> bool:
    """Create new user.

    Arguments:
    ---------
        first_name: User's first name.
        last_name: User's last name.
        email: User's email id.
        password: Password must be encrypted/hashed at frontend.

    Returns:
    ---------
        True if user gets created else False.
    """
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'is_admin': False,
        'is_staff': False
    }
    try:
        response = BASE_USER.put(user)
        profile = {
            'key': response['key'],
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'bio': 'NA',
            'batch': 'NA',
            'linkedin': 'NA',
            'github': 'NA',
            'skills': [],
            'profile_pic': 'NA'
        }
        BASE_PROFILE.put(profile)
    except Exception:  # Type of exception is not provided by deta.
        return False
    return True


def get_user_by_email(email: str) -> Optional[Dict]:
    """Fetch user with matching email id.

    Arguments:
    ---------
        email: User's email id.

    Returns:
    ---------
        User dictionary if user exists else None.
    """
    lst = next(BASE_USER.fetch({'email': email}))
    if lst:
        return lst[0]
    return None


def get_user(key: str) -> Optional[Dict]:
    """Fetch user with matching email id.

    Arguments:
    ---------
        key: User's database key.

    Returns:
    ---------
        User dictionary if user exists else None.
    """
    return BASE_USER.get(key=key)


def delete_user(key: str) -> bool:
    """Delete user with matching email id.

    Arguments:
    ---------
        key: User's database key.

    Returns:
    ---------
        True if user gets deleted else False.
    """
    user = get_user(key=key)
    if not user:
        return False
    BASE_USER.delete(user['key'])
    BASE_PROFILE.delete(user['key'])
    return True


def _update_user(key: str, **kwargs) -> bool:
    """Update user.

    Arguments:
    ---------
        key: Request database key.
        kwargs:
            str => first_name, last_name, email.

    Returns:
    ---------
        True if user get updated else False.
    """
    try:
        BASE_USER.update(updates=kwargs, key=key)
    except Exception:
        return False
    return True


# ========== User Profile ==============================================================================================
def update_profile(key: str, **kwargs) -> bool:
    """Update user profile.

    Arguments:
    ---------
        key: Request database key.
        kwargs:
            str => first_name, last_name, email, bio, linkedin, github, profile_pic.
            List => skills.

    Returns:
    ---------
        True if profile get updated else False.
    """
    try:
        BASE_PROFILE.update(updates=kwargs, key=key)

        # Check if basic parameters need to update.
        user_update = {}
        if 'first_name' in kwargs:
            user_update['first_name'] = kwargs['first_name']
        if 'last_name' in kwargs:
            user_update['last_name'] = kwargs['last_name']
        if 'email' in kwargs:
            user_update['email'] = kwargs['email']
        if user_update:
            _update_user(key=key, **user_update)
    except Exception:
        return False
    return True


def get_profile(key: str) -> Optional[Dict]:
    """Fetch user profile.

    Arguments:
    ---------
        key: User's database key.

    Returns:
    ---------
        Profile dictionary if exists else None.
    """
    return BASE_PROFILE.get(key=key)


# ========== Password ==================================================================================================
def update_password(key: str, new_password: str) -> bool:
    """Delete user with matching email id.

    Arguments:
    ---------
        email: User's email id.

    Returns:
    ---------
        True if password gets updated else False.
    """
    try:
        BASE_USER.update(updates={'password': new_password}, key=key)
    except Exception:  # Type of exception is not provided by deta.
        return False
    return True


def add_password_reset_request(key: str, user_key: str) -> bool:
    """Add password reset request.

    Arguments:
    ---------
        key: Request database key.
        user_key: User's database key.

    Returns:
    ---------
        True if request gets created else False.
    """
    new_request = {
        'key': key,
        'user_key': user_key
    }
    try:
        BASE_PASSWORD_RESET.put(new_request)
    except Exception:  # Type of exception is not provided by deta.
        return False
    return True


def verify_password_reset_request(key: str) -> Optional[Dict]:
    """Fetch request with matching key.
    Remove the request from database.

    Arguments:
    ---------
        key: Request database key.

    Returns:
    ---------
        Request dictionary if exists else None.
    """
    request = BASE_PASSWORD_RESET.get(key=key)
    if request:
        BASE_PASSWORD_RESET.delete(key=key)
    return request
