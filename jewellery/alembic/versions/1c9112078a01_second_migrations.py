"""second migrations

Revision ID: 1c9112078a01
Revises: f91f34e29a43
Create Date: 2024-01-25 18:40:36.424561

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1c9112078a01'
down_revision: Union[str, None] = 'f91f34e29a43'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
