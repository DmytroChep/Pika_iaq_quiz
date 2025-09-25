"""created quiz model and question model

Revision ID: f521cb721488
Revises: 35899dfc77eb
Create Date: 2025-09-24 07:27:35.286236

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f521cb721488'
down_revision: Union[str, None] = '35899dfc77eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
