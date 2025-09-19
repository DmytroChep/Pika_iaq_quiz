"""created quiz model and question model

Revision ID: 337b171ef2f6
Revises: b8359ed432a5
Create Date: 2025-09-19 19:08:57.591346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '337b171ef2f6'
down_revision: Union[str, None] = 'b8359ed432a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
