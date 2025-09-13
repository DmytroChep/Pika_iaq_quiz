"""created quiz model and question model

Revision ID: 0d418ebf202d
Revises: beaa9f75c2e5
Create Date: 2025-09-13 16:16:15.570070

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d418ebf202d'
down_revision: Union[str, None] = 'beaa9f75c2e5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
