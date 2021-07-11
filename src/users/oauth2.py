"""OAuth2 with Password, Bearer with JWT tokens.
"""

# Author Info
__author__ = 'Vishwajeet Ghatage'
__date__ = '10/07/21'
__email__ = 'cloudmail.vishwajeet@gmail.com'

# Library Imports
from datetime import datetime, timedelta
from typing import Dict

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Own Imports
from .. import settings
from . import db

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl='users/login')  # login url


def create_access_token(data: dict) -> str:
    """Create JWT access token.

    Arguments:
    ---------
        data: user email id in dictionary.

    Returns:
    ---------
        JWT Token.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(OAUTH2_SCHEME)) -> Dict:
    """Get current logged in user's data using JWT token.

    Arguments:
    ---------
        token: JWT token.

    Returns:
    ---------
        User dictionary.

    Raises:
    ---------
        HTTPException 401 if not logged in or JWT Error.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user: Dict = db.get_user_by_email(email)
    if user is None:
        raise credentials_exception
    return user
