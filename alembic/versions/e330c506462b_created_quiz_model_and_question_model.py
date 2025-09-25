"""created quiz model and question model

Revision ID: e330c506462b
Revises: 3e784c22c175
Create Date: 2025-09-24 14:32:19.743889

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e330c506462b'
down_revision: Union[str, None] = '3e784c22c175'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
