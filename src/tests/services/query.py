from uuid import UUID

from src.common.services import AbstractRepositoryService
from src.tests.domains import Test
from tests.models import TestModel


class TestsQuery(AbstractRepositoryService):
    async def get_by_id(self, *, test_id: UUID) -> Test | None:
        test = await self.db_session.get(TestModel, test_id)

        return Test.from_orm(test) if test else None
