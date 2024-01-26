"""second migrations

Revision ID: 5b69171db153
Revises: 9af347a06065
Create Date: 2024-01-25 17:42:22.532698

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b69171db153'
down_revision: Union[str, None] = '9af347a06065'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
