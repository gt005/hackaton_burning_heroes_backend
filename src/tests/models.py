from uuid import UUID
from src.database.models import BaseMixin
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class TestModel(BaseMixin):
    __tablename__ = "tests"
    text: Mapped[str] = mapped_column(String(length=30_000))


class TestQuestionModel(BaseMixin):
    __tablename__ = "test_questions"
    test_id: Mapped[UUID] = mapped_column(ForeignKey('tests.id'))
    text: Mapped[str] = mapped_column(String(length=2_000))


class TestResponseOptionModel(BaseMixin):
    __tablename__ = "test_response_options"
    question_id: Mapped[UUID] = mapped_column(ForeignKey('test_questions.id'))
    text: Mapped[str] = mapped_column(String(length=2_000))
    is_correct: Mapped[bool]
