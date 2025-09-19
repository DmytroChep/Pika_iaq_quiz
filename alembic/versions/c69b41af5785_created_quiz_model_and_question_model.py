"""created quiz model and question model

Revision ID: c69b41af5785
Revises: 9bdda2b397dd
Create Date: 2025-09-18 16:49:11.903259

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c69b41af5785'
down_revision: Union[str, None] = '9bdda2b397dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
