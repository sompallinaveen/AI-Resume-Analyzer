from datetime import datetime, timedelta, UTC

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.core.config import settings
from app.crud.user_crud import get_user_by_email
from app.database.dependencies import get_db
from app.models.user import User

# Password hashing
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)

# OAuth2
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM,
    )


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:

    print("\n" + "=" * 70)
    print("get_current_user() called")
    print("=" * 70)

    print("Received Token:")
    print(token)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        print("\nDecoded Payload:")
        print(payload)

        email = payload.get("sub")

        print("\nEmail extracted from token:")
        print(email)

        if email is None:
            print("ERROR: 'sub' claim missing.")
            raise credentials_exception

    except JWTError as e:
        print("\nJWT Decode Error:")
        print(e)
        raise credentials_exception

    user = get_user_by_email(db, email)

    print("\nUser fetched from database:")
    print(user)

    if user is None:
        print("ERROR: User not found.")
        raise credentials_exception

    print("\nAuthentication Successful!")
    print("=" * 70)

    return user