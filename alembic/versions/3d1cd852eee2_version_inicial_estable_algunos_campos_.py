"""Version inicial estable: Algunos campos cambiaron de nombre para una mejor descripcion.

Revision ID: 3d1cd852eee2
Revises: 
Create Date: 2024-05-14 11:58:53.784014

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3d1cd852eee2'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
