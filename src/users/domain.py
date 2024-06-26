from uuid import UUID

from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    hashed_password: str

    class Config:
        from_attributes = True

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return pwd_context.verify(password, hashed_password)


class JWT(BaseModel):
    access_token: str
    refresh_token: str
