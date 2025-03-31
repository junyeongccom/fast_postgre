import os
from fastapi import HTTPException, status
from jose import JWTError, jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

from com.hc_fast.utils.config.security.secret_config import ALGORITHM, SECRET_KEY

load_dotenv()

JWT_SECRET_KEY = os.getenv("SECRET_KEY")
JWT_ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS"))

def create_access_token(data: dict, expires_minutes: int = 15):
    to_encode = data.copy()
    iat = datetime.now(timezone.utc)
    exp = iat + timedelta(minutes=expires_minutes)
    to_encode.update({
        "iat": int(iat.timestamp()),
        "exp": int(exp.timestamp())
    })

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


def create_refresh_token(data: dict, expires_days: int = 7):
    to_encode = data.copy()
    iat = datetime.now(timezone.utc)
    exp = iat + timedelta(days=expires_days)
    to_encode.update({
        "iat": int(iat.timestamp()),
        "exp": int(exp.timestamp())
    })

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="유효하지 않은 인증 토큰입니다.",
            headers={"WWW-Authenticate": "Bearer"},
        )