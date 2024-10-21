"""change names in database

Revision ID: 0da3923e7ff9
Revises: 2282fe19bf2e
Create Date: 2024-10-14 00:12:45.025044

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0da3923e7ff9'
down_revision: Union[str, None] = '2282fe19bf2e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('user_id', sa.Integer(), nullable=True))
    op.add_column('recipes', sa.Column('categoria_id', sa.Integer(), nullable=True))
    op.drop_constraint('recipes_ibfk_2', 'recipes', type_='foreignkey')
    op.drop_constraint('recipes_ibfk_1', 'recipes', type_='foreignkey')
    op.create_foreign_key(None, 'recipes', 'categoryRecipes', ['categoria_id'], ['idCategoryRecipe'])
    op.create_foreign_key(None, 'recipes', 'users', ['user_id'], ['idUser'])
    op.drop_column('recipes', 'userId')
    op.drop_column('recipes', 'categoriaId')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipes', sa.Column('categoriaId', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('recipes', sa.Column('userId', mysql.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.drop_constraint(None, 'recipes', type_='foreignkey')
    op.create_foreign_key('recipes_ibfk_1', 'recipes', 'categoryRecipes', ['categoriaId'], ['idCategoryRecipe'])
    op.create_foreign_key('recipes_ibfk_2', 'recipes', 'users', ['userId'], ['idUser'])
    op.drop_column('recipes', 'categoria_id')
    op.drop_column('recipes', 'user_id')
    # ### end Alembic commands ###