"""Pydantic schemas for Users API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '11/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from typing import List, Optional
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


class ForgotPassword(UserBase):
    """Used to reset password.

    Note:
    ---------
    DOB encryption must be performed at front end.
    """
    pass


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
    email: Optional[EmailStr]
    bio: Optional[str]
    batch: Optional[str]
    linkedin: Optional[str]
    github: Optional[str]
    skills: Optional[List[str]] = ['skill']
