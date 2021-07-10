"""Main functionalities of Auth API.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from fastapi import HTTPException, status
from passlib.context import CryptContext
from typing import Dict

# Own Imports
from . import db, models


CRYPT_CONTEXT = CryptContext(schemes=['bcrypt'], deprecated='auto')


def encrypt_password(password: str) -> str:
    return CRYPT_CONTEXT.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return CRYPT_CONTEXT.verify(password, hashed_password)


def create_user(user_in: models.UserIn):
    if db.get_user(user_in.email):
        raise HTTPException(status.HTTP_409_CONFLICT, detail={'ERROR': 'User already exists.'})
    hashed_password = encrypt_password(user_in.password)
    user_in_db = models.UserInDB(**user_in.dict(), hashed_password=hashed_password)
    return db.create_user(**user_in_db.dict())


def get_user():
    pass
