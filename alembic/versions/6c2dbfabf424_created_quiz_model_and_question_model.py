"""created quiz model and question model

Revision ID: 6c2dbfabf424
Revises: e43e30797caa
Create Date: 2025-09-24 07:51:53.616924

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c2dbfabf424'
down_revision: Union[str, None] = 'e43e30797caa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
