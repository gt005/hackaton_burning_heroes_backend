from uuid import UUID, uuid4

from sqlalchemy import delete

from src.common.services import AbstractRepositoryService
from src.tests.domains import TestResponseOption
from src.tests.models import TestResponseOptionModel


class QuestionResponseCommand(AbstractRepositoryService):
    async def create(
            self,
            *,
            question_id: UUID,
            text: str,
            is_correct: bool,
            commit: bool = True,
    ) -> TestResponseOption:
        question_response = TestResponseOptionModel(
            id=uuid4(),
            question_id=question_id,
            text=text,
            is_correct=is_correct,
        )

        response_option = TestResponseOption.from_orm(question_response)

        self.db_session.add(question_response)
        if commit:
            await self.db_session.commit()

        return response_option

    async def bulk_delete_for_question_id(self, *, question_id: UUID, commit: bool = True) -> None:
        query = delete(TestResponseOptionModel).where(
            TestResponseOptionModel.question_id == question_id
        )

        await self.db_session.execute(query)

        if commit:
            await self.db_session.commit()
