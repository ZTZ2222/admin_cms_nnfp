from datetime import datetime, timedelta, timezone
import jwt

from core.config import settings
from core.models import User
from core.schemas import TokenData
from utils.exceptions import InvalidCredentialsException


class AuthService:
    private_key = settings.auth.private_key_path.read_text()
    public_key = settings.auth.public_key_path.read_text()
    algorithm = settings.auth.algorithm
    lifetime = settings.auth.lifetime

    @classmethod
    def create_access_token(cls, user: User) -> str:
        now = datetime.now(timezone.utc)
        expire = now + timedelta(seconds=cls.lifetime)

        to_encode = {
            "sub": str(user.id),
            "exp": expire,
            "iat": now,
            "iss": "fastapi-local322",
            "username": user.email,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
        }

        return jwt.encode(to_encode, cls.private_key, cls.algorithm)

    @classmethod
    def verify_access_token(cls, token: str) -> TokenData:
        try:
            payload = jwt.decode(token, cls.public_key, algorithms=[cls.algorithm])
            return TokenData(**payload)
        except jwt.PyJWTError:
            raise InvalidCredentialsException
