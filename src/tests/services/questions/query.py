from uuid import UUID

from src.common.services import AbstractRepositoryService
from src.tests.domains import TestQuestion


class QuestionQuery(AbstractRepositoryService):
    async def get_by_id(self, *, question_id: UUID) -> TestQuestion | None:
        db_question = await self.db_session.get(TestQuestion, question_id)

        return TestQuestion.from_orm(db_question) if db_question else None
