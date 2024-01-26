"""second migrations

Revision ID: ad9b0e2d6f6c
Revises: e0f4e6f5766d
Create Date: 2024-01-26 10:05:25.539281

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad9b0e2d6f6c'
down_revision: Union[str, None] = 'e0f4e6f5766d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
