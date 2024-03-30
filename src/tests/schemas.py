from pydantic import BaseModel, Field


class TestCreateSchema(BaseModel):
    text: str
    questions_amount: int = Field(..., ge=1, le=10)
