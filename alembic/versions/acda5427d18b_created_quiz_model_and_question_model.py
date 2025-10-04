"""created quiz model and question model

Revision ID: acda5427d18b
Revises: e330c506462b
Create Date: 2025-09-24 14:38:54.734166

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'acda5427d18b'
down_revision: Union[str, None] = 'e330c506462b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
