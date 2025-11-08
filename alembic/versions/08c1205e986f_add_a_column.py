"""Add a column

Revision ID: 08c1205e986f
Revises: e1f1abca2194
Create Date: 2025-11-08 10:54:01.069246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '08c1205e986f'
down_revision: Union[str, Sequence[str], None] = 'e1f1abca2194'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('articles', sa.Column('last_transaction_date', sa.DateTime))


def downgrade() -> None:
    op.drop_column('articles', 'last_transaction_date')
