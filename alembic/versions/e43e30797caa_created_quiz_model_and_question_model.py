"""created quiz model and question model

Revision ID: e43e30797caa
Revises: 81b2675b91b8
Create Date: 2025-09-24 07:47:47.759458

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e43e30797caa'
down_revision: Union[str, None] = '81b2675b91b8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
