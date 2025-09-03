"""add avatar field

Revision ID: beaa9f75c2e5
Revises: 7ef5b538839b
Create Date: 2025-09-02 17:11:52.346004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'beaa9f75c2e5'
down_revision: Union[str, None] = '7ef5b538839b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
