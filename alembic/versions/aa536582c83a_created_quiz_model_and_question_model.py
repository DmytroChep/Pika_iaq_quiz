"""created quiz model and question model

Revision ID: aa536582c83a
Revises: 16024ca8afa1
Create Date: 2025-09-18 09:16:25.644505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa536582c83a'
down_revision: Union[str, None] = '16024ca8afa1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
