"""Migracion de prueba

Revision ID: aca790af9a4e
Revises: df24769a8c0b
Create Date: 2024-04-16 23:06:24.658217

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aca790af9a4e'
down_revision: Union[str, None] = 'df24769a8c0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('units', sa.Column('segment', sa.String(length=30), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('units', 'segment')
    # ### end Alembic commands ###