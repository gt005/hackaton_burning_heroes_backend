from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import BaseMixin


class UserModel(BaseMixin):
    __tablename__ = "users"
    username: Mapped[str] = mapped_column(String(length=255))
    email: Mapped[str] = mapped_column(String(length=255))
    hashed_password: Mapped[str]
