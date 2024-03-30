from src.tests.domains import Test


class MlTestsQuery:
    async def get_test_from_text(self, text: str, questions_amount: int) -> Test:
        # Call the ml service to get the test
        return Test(text=text, questions=[])
