from src.ml_service.services.query import MlTestsQuery
from src.common.services import AbstractRepositoryService
from src.tests.domains import Test


class TestsCommand(AbstractRepositoryService):
    async def create(self, text: str, questions_amount: int = 10) -> None:
        test: Test = await MlTestsQuery().get_test_from_text(text, questions_amount)
        # TODO: Сделать сохранение в базу

        return test
