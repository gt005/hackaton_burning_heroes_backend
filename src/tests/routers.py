from fastapi import APIRouter, Depends

from src.common.dependencies import get_repository
from src.tests.domains import Test
from src.tests.services.command import TestsCommand
from src.tests.schemas import TestCreateSchema


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
