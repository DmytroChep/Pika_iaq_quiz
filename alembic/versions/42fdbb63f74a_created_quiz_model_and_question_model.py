"""created quiz model and question model

Revision ID: 42fdbb63f74a
Revises: f521cb721488
Create Date: 2025-09-24 07:30:44.696898

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '42fdbb63f74a'
down_revision: Union[str, None] = 'f521cb721488'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
