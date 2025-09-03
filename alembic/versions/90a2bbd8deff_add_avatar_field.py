"""add avatar field

Revision ID: 90a2bbd8deff
Revises: 9e6f8f575cdf
Create Date: 2025-09-02 17:08:52.694574

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90a2bbd8deff'
down_revision: Union[str, None] = '9e6f8f575cdf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
