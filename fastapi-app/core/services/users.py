from typing import Optional, Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import User
from core.schemas import Token, UserCreateWithPassword, UserUpdate
from core.services.oauth2 import AuthService
from utils.security import hash_password, verify_password
from utils.exceptions import InvalidCredentialsException


class UserService:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_create: UserCreateWithPassword) -> User:
        hashed_password = hash_password(user_create.password)
        user_data = user_create.model_dump(exclude={"password"})
        user = User(**user_data, hashed_password=hashed_password)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update_user(self, user_id: int, user_update: UserUpdate) -> User:
        user = await self.session.get(User, user_id)
        if user:
            for field, value in user_update.model_dump().items():
                setattr(user, field, value)
            await self.session.commit()
            await self.session.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> None:
        user = await self.session.get(User, user_id)
        if user:
            await self.session.delete(user)
            await self.session.commit()

    async def find_user(self, **kwargs) -> User:
        stmt = select(User).filter_by(**kwargs)
        return await self.session.scalar(stmt)

    async def get_users_paginated(self, offset: int = 0, limit: int = 10) -> Sequence[User]:
        stmt = select(User) \
            .order_by(User.id) \
            .offset(offset) \
            .limit(limit)
        result = await self.session.scalars(stmt)
        return result.all()

    async def authenticate_user(self, email: str, password: str) -> Optional[Token]:
        user = await self.find_user(email=email)
        if not user or not verify_password(password, user.hashed_password):
            raise InvalidCredentialsException

        access_token = AuthService.create_access_token(user)
        return Token(access_token=access_token)
