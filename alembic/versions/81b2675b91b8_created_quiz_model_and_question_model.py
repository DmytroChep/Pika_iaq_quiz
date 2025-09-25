"""created quiz model and question model

Revision ID: 81b2675b91b8
Revises: 890e6bc87a73
Create Date: 2025-09-24 07:47:20.573965

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '81b2675b91b8'
down_revision: Union[str, None] = '890e6bc87a73'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
