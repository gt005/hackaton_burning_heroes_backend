from pydantic import BaseModel, validator
from pydantic import Field


class TestResponseOption(BaseModel):
    text: str
    is_correct: bool


class TestQuestion(BaseModel):
    text: str
    response_options: list[TestResponseOption]

    @validator('response_options')
    def validate_response_options(cls, response_options):
        num_correct_options = sum(option.is_correct for option in response_options)
        if num_correct_options != 1:
            raise ValueError('Only one response option can be marked as correct')
        return response_options


class Test(BaseModel):
    text: str = Field(..., max_length=30_000)
    questions: list[TestQuestion]
