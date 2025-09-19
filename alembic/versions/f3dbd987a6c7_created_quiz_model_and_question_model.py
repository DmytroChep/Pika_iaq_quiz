"""created quiz model and question model

Revision ID: f3dbd987a6c7
Revises: cbc10829c8c1
Create Date: 2025-09-17 22:31:39.991257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f3dbd987a6c7'
down_revision: Union[str, None] = 'cbc10829c8c1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
