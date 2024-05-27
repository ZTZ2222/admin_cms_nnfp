from typing import Optional
from pydantic import BaseModel, EmailStr

from core.schemas.auth import AuthProvider


class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str]


class UserCreateWithPassword(UserBase):
    password: str
    provider: AuthProvider = AuthProvider.EMAIL


class UserCreateWithSocial(UserBase):
    provider: AuthProvider
    provider_id: str


class UserRead(UserBase):
    id: int
    is_active: bool
    is_superuser: bool

    # instead of
    # class Config:
    #     orm_mode = True
    #
    # we can use, but it set by default
    # model_config = ConfigDict(
    #     from_attributes=True,
    # )


class UserUpdate(UserBase):
    id: int
