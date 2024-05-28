import bcrypt
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User
from core.schemas.users import UserRead
from core.services.oauth2 import AuthService
from utils.exceptions import InvalidCredentialsException

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_password.decode("utf-8")


def verify_password(plain_password, hashed_password) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


async def get_current_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    token: str = Depends(oauth2_scheme),
) -> UserRead:
    token_data = AuthService.verify_access_token(token)

    user_id = token_data.sub
    if user_id is None:
        raise InvalidCredentialsException

    user = await session.get(User, user_id)
    if user is None:
        raise InvalidCredentialsException
    return user
