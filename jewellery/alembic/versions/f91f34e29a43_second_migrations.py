"""second migrations

Revision ID: f91f34e29a43
Revises: 5b69171db153
Create Date: 2024-01-25 18:26:00.395783

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f91f34e29a43'
down_revision: Union[str, None] = '5b69171db153'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
