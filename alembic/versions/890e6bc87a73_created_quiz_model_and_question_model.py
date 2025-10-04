"""created quiz model and question model

Revision ID: 890e6bc87a73
Revises: 42fdbb63f74a
Create Date: 2025-09-24 07:38:18.873451

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '890e6bc87a73'
down_revision: Union[str, None] = '42fdbb63f74a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
