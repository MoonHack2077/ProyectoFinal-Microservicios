# pylint: skip-file
"""second migration

Revision ID: ef109f644376
Revises: 5f80eb428323
Create Date: 2024-10-13 00:57:15.975666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'ef109f644376'
down_revision: Union[str, None] = '5f80eb428323'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('rolId_id', sa.Integer(), nullable=True))
    op.drop_constraint('users_ibfk_2', 'users', type_='foreignkey')
    op.create_foreign_key(None, 'users', 'roles', ['rolId_id'], ['idRole'])
    op.drop_column('users', 'rolId')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('rolId', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.create_foreign_key('users_ibfk_2', 'users', 'roles', ['rolId'], ['idRole'])
    op.drop_column('users', 'rolId_id')
    # ### end Alembic commands ###
