"""Database operations for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import Dict, Optional
from deta import Deta

# Own Imports
from .. import settings

deta = Deta(settings.DETA_ACCESS_KEY)
USERS = deta.Base(settings.BASE_USER)  # Base, similar to collection in MongoDB
PASSWORD_RESET = deta.Base(settings.BASE_PASSWORD_RESET)


def create_user(first_name: str, last_name: str, email: str, dob: str, password: str) -> bool:
    """Create new user.

    Arguments:
    ---------
        first_name: User's first name.
        last_name: User's last name.
        email: User's email id.
        dob: Date of birth, must be encrypted/hashed at frontend.
        password: Password must be encrypted/hashed at frontend.

    Returns:
    ---------
        True if user gets created else False.
    """
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': password,
        'dob': dob,
        'is_admin': False,
    }
    try:
        USERS.put(new_user)
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
    lst = next(USERS.fetch({'email': email}))
    if lst:
        return lst[0]
    return None


def get_user_by_key(key: str) -> Optional[Dict]:
    """Fetch user with matching email id.

    Arguments:
    ---------
        key: User's database key.

    Returns:
    ---------
        User dictionary if user exists else None.
    """
    return USERS.get(key=key)


def delete_user(key: str) -> bool:
    """Delete user with matching email id.

    Arguments:
    ---------
        key: User's database key.

    Returns:
    ---------
        True if user gets deleted else False.
    """
    user = get_user_by_key(key=key)
    if not user:
        return False
    USERS.delete(user['key'])
    return True


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
        USERS.update(updates={'password': new_password}, key=key)
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
        PASSWORD_RESET.put(new_request)
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
    request = PASSWORD_RESET.get(key=key)
    if request:
        PASSWORD_RESET.delete(key=key)
    return request
