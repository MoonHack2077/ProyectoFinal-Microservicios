"""This module contains the classes that represent the database tables in the application."""
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Table, Time, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.settings import DATABASE
Base = declarative_base()


class Role(Base):
    """
    Represents a role in the system.
    Attributes:
        idRole (int): The unique identifier for the role.
        nameRole (str): The name of the role.
        permissions (str): The permissions associated with the role.
    """
    __tablename__ = "roles"
    idRole = Column(Integer, primary_key=True, index=True)
    nameRole = Column(String(255), nullable=False)
    permissions = Column(String(255), nullable=False)

class Family(Base):
    """
    Represents a family entity.
    Attributes:
        idFamily (int): The unique identifier for the family.
        nameFamily (str): The name of the family.
    """

    __tablename__ = "families"
    idFamily = Column(Integer, primary_key=True, index=True)
    nameFamily = Column(String(255), nullable=False)

class User(Base):
    """
    Represents a user in the system.
    Attributes:
        idUser (int): The unique identifier for the user.
        nameUser (str): The name of the user.
        passwordUser (str): The password of the user.
        emailUser (str): The email address of the user.
        photoUser (str): The photo URL of the user.
        rolId (int): The ID of the user's role.
        familyId (int): The ID of the user's family.
    """
    __tablename__ = "users"
    idUser = Column(Integer, primary_key=True, index=True)
    nameUser = Column(String(255), nullable=False)
    passwordUser = Column(String(255), nullable=False)
    emailUser = Column(String(255), nullable=False)
    photoUser = Column(String(255), nullable=False)
    rolId_id = Column(Integer, ForeignKey('roles.idRole'))
    familyId_id = Column(Integer, ForeignKey('families.idFamily'))

class Notification(Base):
    """
    Represents a notification.
    Attributes:
        idNotification (int): The unique identifier of the notification.
        messageNotification (str): The message of the notification.
        dateNotification (datetime.date): The date of the notification.
        userId (int): The ID of the user associated with the notification.
    """
    __tablename__ = "notifications"
    idNotification = Column(Integer, primary_key=True, index=True)
    messageNotification = Column(String(255), nullable=False)
    dateNotification = Column(Date, nullable=False)
    userId = Column(Integer, ForeignKey('users.idUser'))

class Pantry(Base):
    """
    Pantry class represents a pantry in the application.
    Attributes:
        idPantry (int): The unique identifier of the pantry.
        userId (int): The ID of the user associated with the pantry.
    """
    __tablename__ = "pantries"
    idPantry = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey('users.idUser'))

class IngredientInventory(Base):
    """
    Represents an ingredient in the pantry inventory.
    Attributes:
        ingredientId (int): The unique identifier for the ingredient.
        nameIngredient (str): The name of the ingredient.
        amountIngredient (str): The amount of the ingredient.
        unitIngredient (str): The unit of measurement for the ingredient.
        dateExpirationIngredient (datetime.date): The expiration date of the ingredient.
        pantryId (int): The ID of the pantry associated with the ingredient.
    """
    __tablename__ = "ingredient_pantries"
    ingredientId = Column(Integer, primary_key=True, index=True)
    nameIngredient = Column(String(255), nullable=False)
    amountIngredient = Column(String(255), nullable=False)
    unitIngredient = Column(String(255), nullable=False)
    dateExpirationIngredient = Column(Date, nullable=False)
    pantryId = Column(Integer, ForeignKey('pantries.idPantry'))

class CategoryRecipe(Base):
    """
    Represents a category of recipes.
    Attributes:
        idCategoryRecipe (int): The unique identifier of the category recipe.
        nameCategoryRecipe (str): The name of the category recipe.
        descriptionCategoryRecipe (str): The description of the category recipe.
    """

    __tablename__ = "categoryRecipes"
    idCategoryRecipe = Column(Integer, primary_key=True, index=True)
    nameCategoryRecipe = Column(String(255), nullable=False)
    descriptionCategoryRecipe = Column(String(255))

class Recipe(Base):
    """
    Represents a recipe.
    Attributes:
        idRecipe (int): The unique identifier for the recipe.
        nameRecipe (str): The name of the recipe.
        descriptionRecipe (str): The description of the recipe.
        difficultyRecipe (str): The difficulty level of the recipe.
        timePreparation (Time): The time required for preparation.
        instructions (str): The instructions for preparing the recipe.
        nutritionalData (str): The nutritional data of the recipe.
        userId (int): The ID of the user who created the recipe.
        categoriaId (int): The ID of the category to which the recipe belongs.
    """
    __tablename__ = "recipes"
    idRecipe = Column(Integer, primary_key=True, index=True)
    nameRecipe = Column(String(255), nullable=False)
    descriptionRecipe = Column(String(255), nullable=False)
    difficultyRecipe = Column(String(255), nullable=False)
    timePreparation = Column(Time, nullable=False)
    instructions = Column(String(255), nullable=False)
    nutritionalData = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.idUser'))
    categoria_id = Column(Integer, ForeignKey('categoryRecipes.idCategoryRecipe'))

recipe_category_association = Table(
    "category_recipes",
    Base.metadata,
    Column("recetaIdCR", Integer, ForeignKey("recipes.idRecipe")),
    Column("categoriaIdCR", Integer, ForeignKey("categoryRecipes.idCategoryRecipe"))
)

class Menu(Base):
    """
    Represents a menu.
    Attributes:
        idMenu (int): The ID of the menu.
        dateMenu (datetime.date): The date of the menu.
        userId (int): The ID of the user associated with the menu.
    """
    __tablename__ = "menus"
    idMenu = Column(Integer, primary_key=True, index=True)
    dateMenu = Column(Date, nullable=False)
    userId = Column(Integer, ForeignKey('users.idUser'))

menu_recipe_association = Table(
    "menu_recipes",
    Base.metadata,
    Column("menuIdMR", Integer, ForeignKey("menus.idMenu")),
    Column("recipeIdMR", Integer, ForeignKey("recipes.idRecipe"))
)

class ShoppingList(Base):
    """
    Represents a shopping list.
    Attributes:
        idShoppingList (int): The ID of the shopping list (primary key).
        menuId (int): The ID of the associated menu (foreign key).
    """
    __tablename__ = "shopping_lists"
    idShoppingList = Column(Integer, primary_key=True, index=True)
    menuId = Column(Integer, ForeignKey('menus.idMenu'))

class CategoryIngredient(Base):
    """
    Represents a category of ingredients.
    Attributes:
        idCategoryIngredient (int): The unique identifier for the category ingredient.
        nameCategoryIngredient (str): The name of the category ingredient.
        descriptionCategoryIngredient (str): The description of the category ingredient.
    """
    __tablename__ = "categoryIngredients"
    idCategoryIngredient = Column(Integer, primary_key=True, index=True)
    nameCategoryIngredient = Column(String(255), nullable=False)
    descriptionCategoryIngredient = Column(String(255))

class Ingredient(Base):
    """
    Represents an ingredient in a recipe.
    Attributes:
        idIngredient (int): The unique identifier for the ingredient.
        nameIngredient (str): The name of the ingredient.
        amountIngredient (str): The amount of the ingredient.
        unitIngredient (str): The unit of measurement for the ingredient.
        dateExpirationIngredient (Date): The expiration date of the ingredient.
        recipeId (int): The foreign key referencing the recipe the ingredient belongs to.
        categoryIdIngredient (int): The foreign key referencing the category of the ingredient.
    """
    __tablename__ = "ingredients"
    idIngredient = Column(Integer, primary_key=True, index=True)
    nameIngredient = Column(String(255), nullable=False)
    amountIngredient = Column(String(255), nullable=False)
    unitIngredient = Column(String(255), nullable=False)
    dateExpirationIngredient = Column(Date, nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.idRecipe'))
    categoryIngredient_id = Column(Integer, ForeignKey('categoryIngredients.idCategoryIngredient'))

shopping_list_ingredient_association = Table(
    "shopping_list_ingredients",
    Base.metadata,
    Column("shoppingListId", Integer, ForeignKey("shopping_lists.idShoppingList")),
    Column("ingredientId", Integer, ForeignKey("ingredients.idIngredient"))
)
# Configurar la base de datos
DATABASE_URL = f"mysql+pymysql://{DATABASE["user"]}:{DATABASE["password"]}@{DATABASE["host"]}/{DATABASE["name"]}"
engine = create_engine(DATABASE_URL)


# Crear una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
