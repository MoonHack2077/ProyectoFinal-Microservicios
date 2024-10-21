"""This module contains the service functions for the ingredient class."""

from app.models.ingredient_model import Ingredient
from app.config.database import Ingredient as IngredientModel


def create_ingredient_service(ingredient: Ingredient):
    """
    Creates a new ingredient in the database.

    Args:
        ingredient (Ingredient): An object containing the ingredient details.

    Returns:
        IngredientModel: The created ingredient record.
    """
    ingredient_record = IngredientModel.create(
        idIngredient=ingredient.idIngredient,
        nameIngredient=ingredient.nameIngredient,
        amountIngredient=ingredient.amountIngredient,
        unitIngredient=ingredient.unitIngredient,
        dateExpirationIngredient=ingredient.dateExpirationIngredient,
        recipe_id=ingredient.recipe_id,
        categoryIngredient_id=ingredient.categoryIngredient_id
    )
    return ingredient_record


def get_ingredient_service(ingredient_id: int):
    """
    Retrieves an ingredient by its ID.

    Args:
        ingredient_id (int): The unique identifier of the ingredient.

    Returns:
        DICT: A dictionary containing the ingredient's details.

    Raises:
        DoesNotExist: If the ingredient with the given ID does not exist.
    """
    ingredient = IngredientModel.get_by_id(ingredient_id)
    return {
        "idIngredient": ingredient.idIngredient,
        "nameIngredient": ingredient.nameIngredient,
        "amountIngredient": ingredient.amountIngredient,
        "unitIngredient": ingredient.unitIngredient,
        "dateExpirationIngredient": ingredient.dateExpirationIngredient,
        "recipe_id": ingredient.recipe_id,
        "categoryIngredient_id": ingredient.categoryIngredient_id
    }


def get_all_ingredients_service():
    """
    Retrieves all ingredients from the database.

    Returns:
        List: A list of dictionaries containing the data of each ingredient's details.
    """
    ingredients = list(IngredientModel.select())
    return [
        {
            "idIngredient": ingredient.idIngredient,
            "nameIngredient": ingredient.nameIngredient,
            "amountIngredient": ingredient.amountIngredient,
            "unitIngredient": ingredient.unitIngredient,
            "dateExpirationIngredient": ingredient.dateExpirationIngredient,
            "recipe_id": ingredient.recipe_id,
            "categoryIngredient_id": ingredient.categoryIngredient_id
        }
        for ingredient in ingredients
    ]


def update_ingredient_service(ingredient_id: int, ingredient_data: Ingredient):
    """
    Updates an existing ingredient's details by its ID.

    Args:
        ingredient_id (int): The ID of the ingredient to update.
        ingredient_data (Ingredient): An object containing the updated ingredient details.

    Returns:
        IngredientModel: The updated ingredient record.

    Raises:
        DoesNotExist: If the ingredient with the given ID does not exist.
    """
    ingredient = IngredientModel.get_by_id(ingredient_id)
    ingredient.nameIngredient = ingredient_data.nameIngredient
    ingredient.amountIngredient = ingredient_data.amountIngredient
    ingredient.unitIngredient = ingredient_data.unitIngredient
    ingredient.dateExpirationIngredient = ingredient_data.dateExpirationIngredient
    ingredient.recipe_id = ingredient_data.recipe_id
    ingredient.categoryIngredient_id = ingredient_data.categoryIngredient_id
    ingredient.save()
    return ingredient


def delete_ingredient_service(ingredient_id: int):
    """
    Deletes an ingredient from the database by its ID.

    Args:
        ingredient_id (int): The ID of the ingredient to delete.

    Returns:
        dict: A message confirming the deletion.

    Raises:
        DoesNotExist: If the ingredient with the given ID does not exist.
    """
    ingredient = Ingredient.get_by_id(ingredient_id)
    ingredient.delete_instance()
    return {"message": "Ingredient deleted successfully"}
