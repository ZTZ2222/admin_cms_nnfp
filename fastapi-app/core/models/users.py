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
    email: Mapped[str] = mapped_column(
        unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(nullable=True)
    hashed_password: Mapped[str] = mapped_column(nullable=True)
    provider: Mapped[AuthProvider]
    provider_id: Mapped[str] = mapped_column(index=True, nullable=True)
    is_active: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
