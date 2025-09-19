"""created quiz model and question model

Revision ID: b8359ed432a5
Revises: c69b41af5785
Create Date: 2025-09-18 16:49:45.617773

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b8359ed432a5'
down_revision: Union[str, None] = 'c69b41af5785'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
