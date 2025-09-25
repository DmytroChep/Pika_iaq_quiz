"""created quiz model and question model

Revision ID: 3e784c22c175
Revises: 6c2dbfabf424
Create Date: 2025-09-24 08:33:04.294688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e784c22c175'
down_revision: Union[str, None] = '6c2dbfabf424'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
