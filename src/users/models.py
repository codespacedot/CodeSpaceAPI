"""Pydantic schemas for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base User model."""
    email: EmailStr


class UserCreate(UserBase):
    """Used to create user.

    Note:
    ---------
    Password and dob encryption must be performed at front end.
    """
    first_name: str
    last_name: str
    dob: str
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


class ChangePassword(BaseModel):
    """New Password."""
    new_password: str
