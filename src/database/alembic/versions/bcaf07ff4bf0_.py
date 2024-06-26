"""empty message

Revision ID: bcaf07ff4bf0
Revises: 
Create Date: 2024-03-30 20:10:24.080294

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'bcaf07ff4bf0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tests',
    sa.Column('text', sa.String(length=30000), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_questions',
    sa.Column('test_id', sa.Uuid(), nullable=False),
    sa.Column('text', sa.String(length=2000), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['test_id'], ['tests.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_response_options',
    sa.Column('question_id', sa.Uuid(), nullable=False),
    sa.Column('text', sa.String(length=2000), nullable=False),
    sa.Column('is_correct', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=False),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['test_questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_response_options')
    op.drop_table('test_questions')
    op.drop_table('tests')
    # ### end Alembic commands ###
