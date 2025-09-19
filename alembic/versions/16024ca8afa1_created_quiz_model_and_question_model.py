"""created quiz model and question model

Revision ID: 16024ca8afa1
Revises: f3dbd987a6c7
Create Date: 2025-09-18 08:31:49.138272

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16024ca8afa1'
down_revision: Union[str, None] = 'f3dbd987a6c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
