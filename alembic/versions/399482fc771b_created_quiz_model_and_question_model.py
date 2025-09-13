"""created quiz model and question model

Revision ID: 399482fc771b
Revises: 0d418ebf202d
Create Date: 2025-09-13 16:17:47.624028

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '399482fc771b'
down_revision: Union[str, None] = '0d418ebf202d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
