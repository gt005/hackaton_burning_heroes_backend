from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str
    email: str
    password: str


class UserLoginSchema(BaseModel):
    email: str
    password: str


class UserPublicSchema(BaseModel):
    username: str
    email: str
