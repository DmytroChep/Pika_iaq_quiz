"""created quiz model and question model

Revision ID: ce62454b56db
Revises: 337b171ef2f6
Create Date: 2025-09-21 08:41:27.526702

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce62454b56db'
down_revision: Union[str, None] = '337b171ef2f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
