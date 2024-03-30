from uuid import uuid4

from src.tests.domains import Test, TestQuestion, TestResponseOption


class MlTestsQuery:
    async def get_test_from_text(self, text: str, questions_amount: int) -> Test:
        # Call the ml utils to regenerate the question
        return Test(
            id=uuid4(),
            text=text,
            questions=[
                TestQuestion(
                    id=uuid4(),
                    text='Question 1',
                    response_options=[
                        TestResponseOption(id=uuid4(), text='Response 1', is_correct=True),
                        TestResponseOption(id=uuid4(), text='Response 2', is_correct=False),
                        TestResponseOption(id=uuid4(), text='Response 3', is_correct=False),
                        TestResponseOption(id=uuid4(), text='Response 4', is_correct=False),
                    ]
                ),
                TestQuestion(
                    id=uuid4(),
                    text='Question 2',
                    response_options=[
                        TestResponseOption(id=uuid4(), text='Response 1', is_correct=False),
                        TestResponseOption(id=uuid4(), text='Response 2', is_correct=True),
                        TestResponseOption(id=uuid4(), text='Response 3', is_correct=False),
                        TestResponseOption(id=uuid4(), text='Response 4', is_correct=False),
                    ]
                ),
            ]
        )

    async def regenerate_question(self, test: Test, question: TestQuestion) -> TestQuestion:
        # Call the ml utils to regenerate the question
        return TestQuestion(
            id=question.id,
            text=question.text,
            response_options=[
                TestResponseOption(id=uuid4(), text='Response 1', is_correct=True),
                TestResponseOption(id=uuid4(), text='Response 2', is_correct=False),
                TestResponseOption(id=uuid4(), text='Response 3', is_correct=False),
                TestResponseOption(id=uuid4(), text='Response 4', is_correct=False),
            ]
        )
