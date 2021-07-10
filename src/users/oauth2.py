from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from . import db, models
from .. import settings

OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl='users/login')


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(OAUTH2_SCHEME)):
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
    user = models.UserLoginOut(**db.get_user(email))
    if user is None:
        raise credentials_exception
    return user
