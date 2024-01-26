"""second migrations

Revision ID: e0f4e6f5766d
Revises: 1c9112078a01
Create Date: 2024-01-26 10:01:15.107463

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0f4e6f5766d'
down_revision: Union[str, None] = '1c9112078a01'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
