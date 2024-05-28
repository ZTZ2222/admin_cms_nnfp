from typing import Optional
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from core.schemas.auth import AuthProvider
from core.models import Base
from core.models.mixins import (
    PkIdIntMixin,
    TimestampMixin,
)


class User(Base, PkIdIntMixin, TimestampMixin):
    email: Mapped[str] = mapped_column(unique=True, index=True)
    name: Mapped[Optional[str]]
    hashed_password: Mapped[Optional[str]]
    provider: Mapped[AuthProvider]
    provider_id: Mapped[Optional[str]] = mapped_column(unique=True)
    is_active: Mapped[bool] = mapped_column(default=False, server_default="false")
    is_superuser: Mapped[bool] = mapped_column(default=False, server_default="false")
