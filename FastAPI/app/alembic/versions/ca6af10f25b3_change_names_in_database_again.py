"""change names in database again

Revision ID: ca6af10f25b3
Revises: 533eb3c58de9
Create Date: 2024-10-21 15:22:22.754308

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'ca6af10f25b3'
down_revision: Union[str, None] = '533eb3c58de9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ingredient_pantries', sa.Column('pantry_id', sa.Integer(), nullable=True))
    op.drop_constraint('ingredient_pantries_ibfk_1', 'ingredient_pantries', type_='foreignkey')
    op.create_foreign_key(None, 'ingredient_pantries', 'pantries', ['pantry_id'], ['idPantry'])
    op.drop_column('ingredient_pantries', 'pantryId')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ingredient_pantries', sa.Column('pantryId', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'ingredient_pantries', type_='foreignkey')
    op.create_foreign_key('ingredient_pantries_ibfk_1', 'ingredient_pantries', 'pantries', ['pantryId'], ['idPantry'])
    op.drop_column('ingredient_pantries', 'pantry_id')
    # ### end Alembic commands ###