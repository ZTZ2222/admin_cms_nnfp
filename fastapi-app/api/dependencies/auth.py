from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User
from core.schemas.users import UserRead
from core.services.oauth2 import AuthService
from utils.exceptions import InvalidCredentialsException, UnauthorizedAccessException


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


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


async def get_current_active_user(
    current_user: UserRead = Depends(get_current_user),
) -> UserRead:
    if not current_user.is_active:
        raise UnauthorizedAccessException
    return current_user


async def get_current_admin_user(
    current_user: UserRead = Depends(get_current_user),
) -> UserRead:
    if not current_user.is_superuser:
        raise UnauthorizedAccessException
    return current_user
