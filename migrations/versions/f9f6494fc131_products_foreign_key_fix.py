"""Products foreign key fix

Revision ID: f9f6494fc131
Revises: f426d7c3908f
Create Date: 2024-02-07 10:06:05.943343

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f9f6494fc131'
down_revision: Union[str, None] = 'f426d7c3908f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('products', 'desert_id', new_column_name='dessert_id', existing_type=sa.Integer(), existing_nullable=True)


def downgrade():
    op.alter_column('products', 'dessert_id', new_column_name='desert_id', existing_type=sa.Integer(), existing_nullable=True)
