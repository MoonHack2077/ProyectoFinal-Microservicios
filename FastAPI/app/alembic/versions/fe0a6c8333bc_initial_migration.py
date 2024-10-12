"""Initial migration

Revision ID: fe0a6c8333bc
Revises: 
Create Date: 2024-10-10 16:00:07.216830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe0a6c8333bc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categoryIngredients',
    sa.Column('idCategoryIngredient', sa.Integer(), nullable=False),
    sa.Column('nameCategoryIngredient', sa.String(length=255), nullable=False),
    sa.Column('descriptionCategoryIngredient', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('idCategoryIngredient')
    )
    op.create_index(op.f('ix_categoryIngredients_idCategoryIngredient'), 'categoryIngredients', ['idCategoryIngredient'], unique=False)
    op.create_table('categoryRecipes',
    sa.Column('idCategoryRecipe', sa.Integer(), nullable=False),
    sa.Column('nameCategoryRecipe', sa.String(length=255), nullable=False),
    sa.Column('descriptionCategoryRecipe', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('idCategoryRecipe')
    )
    op.create_index(op.f('ix_categoryRecipes_idCategoryRecipe'), 'categoryRecipes', ['idCategoryRecipe'], unique=False)
    op.create_table('families',
    sa.Column('idFamily', sa.Integer(), nullable=False),
    sa.Column('nameFamily', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('idFamily')
    )
    op.create_index(op.f('ix_families_idFamily'), 'families', ['idFamily'], unique=False)
    op.create_table('roles',
    sa.Column('idRole', sa.Integer(), nullable=False),
    sa.Column('nameRole', sa.String(length=255), nullable=False),
    sa.Column('permissions', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('idRole')
    )
    op.create_index(op.f('ix_roles_idRole'), 'roles', ['idRole'], unique=False)
    op.create_table('users',
    sa.Column('idUser', sa.Integer(), nullable=False),
    sa.Column('nameUser', sa.String(length=255), nullable=False),
    sa.Column('passwordUser', sa.String(length=255), nullable=False),
    sa.Column('emailUser', sa.String(length=255), nullable=False),
    sa.Column('photoUser', sa.String(length=255), nullable=False),
    sa.Column('rolId', sa.Integer(), nullable=True),
    sa.Column('familyId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['familyId'], ['families.idFamily'], ),
    sa.ForeignKeyConstraint(['rolId'], ['roles.idRole'], ),
    sa.PrimaryKeyConstraint('idUser')
    )
    op.create_index(op.f('ix_users_idUser'), 'users', ['idUser'], unique=False)
    op.create_table('menus',
    sa.Column('idMenu', sa.Integer(), nullable=False),
    sa.Column('dateMenu', sa.Date(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.idUser'], ),
    sa.PrimaryKeyConstraint('idMenu')
    )
    op.create_index(op.f('ix_menus_idMenu'), 'menus', ['idMenu'], unique=False)
    op.create_table('notifications',
    sa.Column('idNotification', sa.Integer(), nullable=False),
    sa.Column('messageNotification', sa.String(length=255), nullable=False),
    sa.Column('dateNotification', sa.Date(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.idUser'], ),
    sa.PrimaryKeyConstraint('idNotification')
    )
    op.create_index(op.f('ix_notifications_idNotification'), 'notifications', ['idNotification'], unique=False)
    op.create_table('pantries',
    sa.Column('idPantry', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.idUser'], ),
    sa.PrimaryKeyConstraint('idPantry')
    )
    op.create_index(op.f('ix_pantries_idPantry'), 'pantries', ['idPantry'], unique=False)
    op.create_table('recipes',
    sa.Column('idRecipe', sa.Integer(), nullable=False),
    sa.Column('nameRecipe', sa.String(length=255), nullable=False),
    sa.Column('descriptionRecipe', sa.String(length=255), nullable=False),
    sa.Column('difficultyRecipe', sa.String(length=255), nullable=False),
    sa.Column('timePreparation', sa.Time(), nullable=False),
    sa.Column('instructions', sa.String(length=255), nullable=False),
    sa.Column('nutritionalData', sa.String(length=255), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('categoriaId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoriaId'], ['categoryRecipes.idCategoryRecipe'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.idUser'], ),
    sa.PrimaryKeyConstraint('idRecipe')
    )
    op.create_index(op.f('ix_recipes_idRecipe'), 'recipes', ['idRecipe'], unique=False)
    op.create_table('category_recipes',
    sa.Column('recetaIdCR', sa.Integer(), nullable=True),
    sa.Column('categoriaIdCR', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoriaIdCR'], ['categoryRecipes.idCategoryRecipe'], ),
    sa.ForeignKeyConstraint(['recetaIdCR'], ['recipes.idRecipe'], )
    )
    op.create_table('ingredient_pantries',
    sa.Column('ingredientId', sa.Integer(), nullable=False),
    sa.Column('nameIngredient', sa.String(length=255), nullable=False),
    sa.Column('amountIngredient', sa.String(length=255), nullable=False),
    sa.Column('unitIngredient', sa.String(length=255), nullable=False),
    sa.Column('dateExpirationIngredient', sa.Date(), nullable=False),
    sa.Column('pantryId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pantryId'], ['pantries.idPantry'], ),
    sa.PrimaryKeyConstraint('ingredientId')
    )
    op.create_index(op.f('ix_ingredient_pantries_ingredientId'), 'ingredient_pantries', ['ingredientId'], unique=False)
    op.create_table('ingredients',
    sa.Column('idIngredient', sa.Integer(), nullable=False),
    sa.Column('nameIngredient', sa.String(length=255), nullable=False),
    sa.Column('amountIngredient', sa.String(length=255), nullable=False),
    sa.Column('unitIngredient', sa.String(length=255), nullable=False),
    sa.Column('dateExpirationIngredient', sa.Date(), nullable=False),
    sa.Column('recipeId', sa.Integer(), nullable=True),
    sa.Column('categoryIdIngredient', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['categoryIdIngredient'], ['categoryIngredients.idCategoryIngredient'], ),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.idRecipe'], ),
    sa.PrimaryKeyConstraint('idIngredient')
    )
    op.create_index(op.f('ix_ingredients_idIngredient'), 'ingredients', ['idIngredient'], unique=False)
    op.create_table('menu_recipes',
    sa.Column('menuIdMR', sa.Integer(), nullable=True),
    sa.Column('recipeIdMR', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menuIdMR'], ['menus.idMenu'], ),
    sa.ForeignKeyConstraint(['recipeIdMR'], ['recipes.idRecipe'], )
    )
    op.create_table('shopping_lists',
    sa.Column('idShoppingList', sa.Integer(), nullable=False),
    sa.Column('menuId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['menuId'], ['menus.idMenu'], ),
    sa.PrimaryKeyConstraint('idShoppingList')
    )
    op.create_index(op.f('ix_shopping_lists_idShoppingList'), 'shopping_lists', ['idShoppingList'], unique=False)
    op.create_table('shopping_list_ingredients',
    sa.Column('shoppingListId', sa.Integer(), nullable=True),
    sa.Column('ingredientId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredientId'], ['ingredients.idIngredient'], ),
    sa.ForeignKeyConstraint(['shoppingListId'], ['shopping_lists.idShoppingList'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_list_ingredients')
    op.drop_index(op.f('ix_shopping_lists_idShoppingList'), table_name='shopping_lists')
    op.drop_table('shopping_lists')
    op.drop_table('menu_recipes')
    op.drop_index(op.f('ix_ingredients_idIngredient'), table_name='ingredients')
    op.drop_table('ingredients')
    op.drop_index(op.f('ix_ingredient_pantries_ingredientId'), table_name='ingredient_pantries')
    op.drop_table('ingredient_pantries')
    op.drop_table('category_recipes')
    op.drop_index(op.f('ix_recipes_idRecipe'), table_name='recipes')
    op.drop_table('recipes')
    op.drop_index(op.f('ix_pantries_idPantry'), table_name='pantries')
    op.drop_table('pantries')
    op.drop_index(op.f('ix_notifications_idNotification'), table_name='notifications')
    op.drop_table('notifications')
    op.drop_index(op.f('ix_menus_idMenu'), table_name='menus')
    op.drop_table('menus')
    op.drop_index(op.f('ix_users_idUser'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_idRole'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_families_idFamily'), table_name='families')
    op.drop_table('families')
    op.drop_index(op.f('ix_categoryRecipes_idCategoryRecipe'), table_name='categoryRecipes')
    op.drop_table('categoryRecipes')
    op.drop_index(op.f('ix_categoryIngredients_idCategoryIngredient'), table_name='categoryIngredients')
    op.drop_table('categoryIngredients')
    # ### end Alembic commands ###