"""Добавление новой таблицы

Revision ID: 9e6f8f575cdf
Revises: 5e0ff4a4a7c7
Create Date: 2025-08-30 13:55:13.202781

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9e6f8f575cdf'
down_revision: Union[str, None] = '5e0ff4a4a7c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
