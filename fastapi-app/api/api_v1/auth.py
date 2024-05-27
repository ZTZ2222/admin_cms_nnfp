from typing import Annotated
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from core.config import settings
from core.models import db_helper
from core.schemas import Token
from core.services import UserService


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
        email=user_credentials.username,
        password=user_credentials.password
    )
    return token
