from uuid import UUID

from pydantic import BaseModel, Field, validator


class TestResponseOption(BaseModel):
    id: UUID
    text: str
    is_correct: bool


class TestQuestion(BaseModel):
    id: UUID
    text: str
    response_options: list[TestResponseOption]

    @validator('response_options')
    def validate_response_options(cls, response_options):
        num_correct_options = sum(option.is_correct for option in response_options)
        if num_correct_options != 1:
            raise ValueError('Only one response option can be marked as correct')
        return response_options


class Test(BaseModel):
    id: UUID
    text: str = Field(..., max_length=30_000)
    user_creator_id: UUID | None = None
    questions: list[TestQuestion]
