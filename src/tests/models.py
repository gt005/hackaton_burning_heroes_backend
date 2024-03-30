from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models import BaseMixin


class TestModel(BaseMixin):
    __tablename__ = "tests"
    text: Mapped[str] = mapped_column(String(length=30_000))
    user_creator_id: Mapped[UUID | None] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))


class TestQuestionModel(BaseMixin):
    __tablename__ = "test_questions"
    test_id: Mapped[UUID] = mapped_column(ForeignKey('tests.id', ondelete='CASCADE'))
    text: Mapped[str] = mapped_column(String(length=2_000))


class TestResponseOptionModel(BaseMixin):
    __tablename__ = "test_response_options"
    question_id: Mapped[UUID] = mapped_column(ForeignKey('test_questions.id', ondelete='CASCADE'))
    text: Mapped[str] = mapped_column(String(length=2_000))
    is_correct: Mapped[bool]
