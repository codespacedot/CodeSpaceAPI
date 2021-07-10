"""Database operations for Auth API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from deta import Deta
from typing import Dict, Union

# Own Imports
from .. import settings

deta = Deta(settings.DETA_ACCESS_KEY)
USERS = deta.Base(settings.BASE_USER)  # Base, similar to collection in MongoDB


def create_user(first_name: str, last_name: str, email: str, hashed_password: str, is_admin: bool = False,
                is_staff: bool = False) -> Dict:
    new_user = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': hashed_password,
        'is_admin': is_admin,
        'is_staff': is_staff
    }
    USERS.put(new_user)
    return next(USERS.fetch({'email': email}))[0]


def get_user(email: str) -> Union[Dict, None]:
    lst = next(USERS.fetch({'email': email}))
    if lst:
        return lst[0]
    return None


def delete_user(key: str) -> bool:
    user = USERS.get(key)
    if not user:
        return False
    USERS.delete(key)
    return True
