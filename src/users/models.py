"""Pydantic schemas for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional


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


class ForgotPassword(BaseModel):
    """Used to reset password.

    Note:
    ---------
    DOB encryption must be performed at front end.
    """
    email: EmailStr
    dob: str


class ResetPassword(ChangePassword):
    """Password reset request."""
    verification_code: str


class ProfileGet(BaseModel):
    """Used to get user profile."""
    name: str
    email: EmailStr
    bio: str
    batch: str
    linkedin: str
    github: str
    skills: List[str]
    profile_pic: str


class ProfileUpdate(BaseModel):
    """Used to update user profile."""
    first_name: Optional[str]
    last_name: Optional[str]
    bio: Optional[str]
    batch: Optional[str]
    linkedin: Optional[HttpUrl]
    github: Optional[HttpUrl]
    skills: Optional[List[str]]
