"""Pydantic schemas for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from pydantic import BaseModel


class UserBase(BaseModel):
    """Base User model."""
    email: str


class UserCreate(UserBase):
    """Used to create user.

    Note:
    ---------
    Password encryption must be performed at front end.
    """
    first_name: str
    last_name: str
    password: str


class UserLogin(UserBase):
    """Used to login user.

    Note:
    ---------
    Password encryption must be performed at front end.
    """
    password: str


class Token(BaseModel):
    """JWT Token."""
    access_token: str
    token_type: str
