from pydantic import BaseModel, Field, validator


class TestCreateSchema(BaseModel):
    text: str
    questions_amount: int = Field(..., ge=1, le=10)


class TestResponseOptionUpdateSchema(BaseModel):
    text: str
    is_correct: bool


class QuestionUpdateSchema(BaseModel):
    text: str
    response_options: list[TestResponseOptionUpdateSchema]

    @validator('response_options')
    def validate_response_options(cls, response_options):
        num_correct_options = sum(option.is_correct for option in response_options)
        if num_correct_options != 1:
            raise ValueError('Only one response option can be marked as correct')
        return response_options
