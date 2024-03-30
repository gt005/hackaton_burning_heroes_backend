from uuid import UUID

from sqlalchemy import select

from src.common.services import AbstractRepositoryService
from src.users.domain import User
from src.users.models import UserModel


class UserQuery(AbstractRepositoryService):
    async def get_by_id(self, *, user_id: UUID) -> User | None:
        user = await self.db_session.get(UserModel, user_id)

        return User.from_orm(user) if user else None

    async def get_by_email(self, *, email: str) -> User | None:
        query = select(UserModel).where(UserModel.email == email)
        user: UserModel = await self.db_session.scalar(query)

        if user is None:
            return

        return User.from_orm(user)
