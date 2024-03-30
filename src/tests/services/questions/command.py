from uuid import UUID, uuid4

from sqlalchemy import delete, update

from src.common.services import AbstractRepositoryService
from src.ml_service.services.query import MlTestsQuery
from src.tests.domains import Test, TestQuestion, TestResponseOption
from src.tests.models import TestQuestionModel
from src.tests.services.question_responses.command import QuestionResponseCommand


class QuestionCommand(AbstractRepositoryService):
    async def create(
            self,
            test_id: UUID,
            text: str,
            question_responses: list[TestResponseOption],
    ) -> TestQuestion:
        created_question = TestQuestionModel(
            id=uuid4(),
            test_id=test_id,
            text=text
        )
        self.db_session.add(created_question)
        await self.db_session.commit()

        question_response_command = QuestionResponseCommand(db_session=self.db_session)
        for response in question_responses:
            await question_response_command.create(
                question_id=created_question.id,
                text=response.text,
                is_correct=response.is_correct,
                commit=False
            )

        await self.db_session.commit()

        test_question = TestQuestion(
            id=created_question.id,
            text=text,
            responses=question_responses
        )

        return test_question

    async def update(
            self,
            *,
            id: UUID,
            text: str,
            question_responses: list[TestResponseOption],
    ) -> TestQuestion:
        query = update(TestQuestionModel).where(TestQuestionModel.id == id).values(
            text=text,
        )
        await self.db_session.execute(query)

        question_response_command = QuestionResponseCommand(db_session=self.db_session)
        await question_response_command.bulk_delete_for_question_id(question_id=id, commit=False)

        for i, response in enumerate(question_responses):
            await question_response_command.create(
                question_id=id,
                text=response.text,
                is_correct=response.is_correct,
                commit=False
            )
            question_responses[i] = response

        await self.db_session.commit()

        test_question = TestQuestion(
            id=id,
            text=text,
            responses=question_responses
        )

        return test_question

    async def regenerate(self, test: Test, question: TestQuestion) -> TestQuestion:
        regenerated_question = await MlTestsQuery().regenerate_question(
            test=test,
            question=question
        )

        await self.delete(question_id=question.id)
        created_question = await self.create(
            test_id=test.id,
            text=regenerated_question.text,
            question_responses=regenerated_question.response_options
        )

        return created_question

    async def delete(self, question_id: UUID) -> None:
        query = delete(TestQuestionModel).where(TestQuestionModel.id == question_id)
        await self.db_session.execute(query)
        await self.db_session.commit()
