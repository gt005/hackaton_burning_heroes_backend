from uuid import UUID

from fastapi import APIRouter, Depends

from src.common.dependencies import (
    get_current_user_id_from_access_token,
    get_repository,
)
from src.exceptions import BadRequest
from src.users.domain import JWT, User
from src.users.schemas import UserCreateSchema, UserLoginSchema, UserPublicSchema
from src.users.services.jwt.command import JWTCommand
from src.users.services.users.command import UserCommand
from src.users.services.users.query import UserQuery


user_v1_router = APIRouter(tags=['users'])


@user_v1_router.post('/registration')
async def create_user(
        user_create_schema: UserCreateSchema,
        user_command: UserCommand = Depends(get_repository(UserCommand))
) -> JWT:
    user: User = await user_command.create(
        email=user_create_schema.email,
        username=user_create_schema.username,
        password=user_create_schema.password
    )

    return JWTCommand().create(user_id=user.id)


@user_v1_router.post('/login')
async def login(
        user_create_schema: UserLoginSchema,
        user_query: UserQuery = Depends(get_repository(UserQuery))
) -> JWT:
    user = await user_query.get_by_email(email=user_create_schema.email)

    if user is None or not user.verify_password(
        user_create_schema.password,
        user.hashed_password
    ):
        raise BadRequest()

    return JWTCommand().create(user_id=user.id)


@user_v1_router.get('/me')
async def me(
        user_id: UUID = Depends(get_current_user_id_from_access_token),
        user_query: UserQuery = Depends(get_repository(UserQuery))
) -> UserPublicSchema:
    user = await user_query.get_by_id(user_id=user_id)

    if user is None:
        raise BadRequest()

    return UserPublicSchema(**user.model_dump())
