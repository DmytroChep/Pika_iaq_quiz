"""created quiz model and question model

Revision ID: 11d4316b6e3e
Revises: acda5427d18b
Create Date: 2025-09-24 14:41:51.927259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11d4316b6e3e'
down_revision: Union[str, None] = 'acda5427d18b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
