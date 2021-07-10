"""Pydantic schemas for Auth API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserIn(UserBase):
    password: str


class UserDBIn(UserBase):
    hashed_password: str


class UserOut(UserBase):
    key: str


class UserLoginIn(BaseModel):
    email: str
    password: str


class UserLoginOut(UserOut):
    is_admin: bool
    is_staff: bool
