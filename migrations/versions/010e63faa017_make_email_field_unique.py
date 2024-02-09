"""Make email field unique

Revision ID: 010e63faa017
Revises: f9f6494fc131
Create Date: 2024-02-08 16:19:37.087909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '010e63faa017'
down_revision: Union[str, None] = 'f9f6494fc131'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# Этот метод будет вызван при применении миграции
def upgrade():
    op.create_unique_constraint("uq_user_email", "user", ["email"])


# Этот метод будет вызван при откате миграции
def downgrade():
    op.drop_constraint("uq_user_email", "user", type_="unique")
