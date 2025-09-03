"""add avatar field

Revision ID: 7ef5b538839b
Revises: 90a2bbd8deff
Create Date: 2025-09-02 17:11:26.232661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ef5b538839b'
down_revision: Union[str, None] = '90a2bbd8deff'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
