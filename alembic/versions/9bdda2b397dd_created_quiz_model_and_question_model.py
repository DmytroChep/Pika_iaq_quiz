"""created quiz model and question model

Revision ID: 9bdda2b397dd
Revises: aa536582c83a
Create Date: 2025-09-18 09:21:17.919247

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9bdda2b397dd'
down_revision: Union[str, None] = 'aa536582c83a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
