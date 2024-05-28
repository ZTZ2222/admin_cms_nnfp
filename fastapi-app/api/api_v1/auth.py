from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas import Token
from core.schemas.users import UserCreateWithPassword
from core.services import UserService
from core.services.oauth2 import AuthService


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["auth"],
)


@router.post("/login", response_model=Token)
async def login(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_credentials: OAuth2PasswordRequestForm = Depends(),
):
    user_service = UserService(session=session)
    token = await user_service.authenticate_user(
        email=user_credentials.username, password=user_credentials.password
    )
    return token


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=Token)
async def signup(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
    user_create: OAuth2PasswordRequestForm = Depends(),
):
    user_service = UserService(session=session)
    user = await user_service.create_user(
        user_create=UserCreateWithPassword(
            email=user_create.username, password=user_create.password
        )
    )

    token = AuthService.create_access_token(user)
    return Token(access_token=token)
