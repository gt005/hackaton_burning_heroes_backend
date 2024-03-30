from uuid import UUID

from fastapi import APIRouter, Depends

from src.common.dependencies import get_repository
from src.exceptions import BadRequest
from src.tests.domains import Test, TestQuestion
from src.tests.schemas import QuestionUpdateSchema, TestCreateSchema
from src.tests.services.command import TestsCommand
from src.tests.services.query import TestsQuery
from src.tests.services.questions.command import QuestionCommand
from src.tests.services.questions.query import QuestionQuery


tests_v1_router = APIRouter(tags=['tests'])


@tests_v1_router.post('/')
async def create_text_from_text(
    test_create_schema: TestCreateSchema,
    tests_command: TestsCommand = Depends(get_repository(TestsCommand))
) -> Test:
    created_test: Test = await tests_command.create(
        text=test_create_schema.text,
        questions_amount=test_create_schema.questions_amount
    )
    return created_test


@tests_v1_router.put('/{test_id}/questions/{question_id}')
async def edit_question(
    test_id: UUID,
    question_id: UUID,
    question_update_schema: QuestionUpdateSchema,
    question_query: QuestionQuery = Depends(get_repository(QuestionQuery)),
    question_command: QuestionCommand = Depends(get_repository(QuestionCommand))
) -> TestQuestion:
    question = await question_query.get_by_id(question_id=question_id)

    if question is None:
        raise BadRequest()

    test_question = await question_command.update(
        id=question_id,
        text=question_update_schema.text,
        question_responses=question_update_schema.response_options
    )

    return test_question


@tests_v1_router.put('/{test_id}/regenerate/{question_id}')
async def regenerate_question(
    test_id: UUID,
    question_id: UUID,
    question_query: QuestionQuery = Depends(get_repository(QuestionQuery)),
    question_command: QuestionCommand = Depends(get_repository(QuestionCommand)),
    test_query: TestsQuery = Depends(get_repository(TestsQuery))
) -> TestQuestion:
    question = await question_query.get_by_id(question_id=question_id)
    if question is None:
        raise BadRequest()

    test = await test_query.get_by_id(test_id=test_id)

    test_question = await question_command.regenerate(test=test, question=question)

    return test_question
