"""created quiz model and question model

Revision ID: 35899dfc77eb
Revises: ce62454b56db
Create Date: 2025-09-21 21:52:55.372980

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35899dfc77eb'
down_revision: Union[str, None] = 'ce62454b56db'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
