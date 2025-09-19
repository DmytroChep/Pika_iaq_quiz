"""created quiz model and question model

Revision ID: cbc10829c8c1
Revises: 399482fc771b
Create Date: 2025-09-14 16:35:07.551665

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbc10829c8c1'
down_revision: Union[str, None] = '399482fc771b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
