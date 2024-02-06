"""new pass length

Revision ID: f426d7c3908f
Revises: 
Create Date: 2024-02-06 20:35:49.694747

"""
from typing import Sequence, Union

from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'f426d7c3908f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Изменяем тип столбца пароля на VARCHAR(255)
    op.alter_column('user', 'password',
                    existing_type=mysql.VARCHAR(length=45),
                    type_=mysql.VARCHAR(length=255),
                    existing_nullable=True)

    # Проверяем существование индекса перед его удалением
    if op.get_bind().engine.dialect.has_index(op.get_bind(), "user", "ix_user_password"):
        # Удаляем существующий индекс для столбца пароля
        op.drop_index(op.f('ix_user_password'), table_name='user')

    # Создаем новый индекс для столбца пароля с учетом новой длины
    op.create_index(op.f('ix_user_password'), 'user', ['password'], unique=False)


def downgrade() -> None:
    # Проверяем существование индекса перед его удалением
    if op.get_bind().engine.dialect.has_index(op.get_bind(), "user", "ix_user_password"):
        # Удаляем существующий индекс для столбца пароля
        op.drop_index('ix_user_password', table_name='user')

    # Создаем новый индекс для столбца пароля с учетом предыдущей длины
    op.create_index('ix_user_password', 'user', ['password'], unique=False)

    # ### end Alembic commands ###
