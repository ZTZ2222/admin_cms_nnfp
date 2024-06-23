import enum
from typing import Optional

from pydantic import BaseModel


class AuthProvider(enum.Enum):
    EMAIL = "email"
    GOOGLE = "google"
    FACEBOOK = "facebook"


class Token(BaseModel):
    access_token: str
    token_type: str = "Bearer"


class TokenData(BaseModel):
    sub: int
    exp: int
    iat: int
    iss: str
    username: str
    is_active: bool
    is_superuser: bool
