"""This module contains the service functions for the recipe model."""

from app.models.recipe_model import Recipe
from app.config.database import Recipe as RecipeModel


def create_recipe_service(recipe: Recipe):
    """
    Creates a new recipe in the database.

    Args:
        recipe (Recipe): An object containing the recipe details.

    Returns:
        RecipeModel: The created recipe record.
    """
    recipe_record = RecipeModel.create(
        idRecipe=recipe.idRecipe,
        nameRecipe=recipe.nameRecipe,
        descriptionRecipe=recipe.descriptionRecipe,
        difficultyRecipe=recipe.difficultyRecipe,
        timePreparation=recipe.timePreparation,
        instructions=recipe.instructions,
        nutritionalData=recipe.nutritionalData,
        user_id = recipe.userId,
        categoria_id = recipe.categoriaId
    )
    return recipe_record


def get_recipe_service(recipe_id: int):
    """
    Retrieves a user by their ID.

    Args:
        recipe_id (int): The unique identifier of the user.

    Returns:
        DICT: A dictionary containing the recipe's details.

    Raises:
        DoesNotExist: If the recipe with the given ID does not exist.
    """
    recipe = RecipeModel.get_by_id(recipe_id)
    return {
        "idRecipe": recipe.idRecipe,
        "nameRecipe": recipe.nameRecipe,
        "descriptionRecipe": recipe.descriptionRecipe,
        "difficulty": recipe.difficultyRecipe,
        "timePreparation": recipe.timePreparation,
        "instructions": recipe.instructions,
        "nutritionalData": recipe.nutritionalData,
        "user_id" : recipe.user_id,
        "categoria_id" : recipe.categoria_id
    }


def get_all_recipes_service():
    """
    Retrieves all recipes from the database.

    Returns:
        List: A list of dictionaries containing the data of each recipe's details.
    """
    recipes = list(RecipeModel.select())
    return [
        {
            "id": recipe.idRecipe,
            "name": recipe.nameRecipe,
            "description": recipe.descriptionRecipe,
            "difficulty": recipe.difficultyRecipe,
            "timePreparation": recipe.timePreparation,
            "instructions": recipe.instructions,
            "nutritionalData": recipe.nutritionalData,
            "user_id" : recipe.user_id,
            "categoria_id" : recipe.categoria_id
        }
        for recipe in recipes
    ]


def update_recipe_service(recipe_id: int, recipe_data: Recipe):
    """
    Updates an existing recipe's details by their ID.

    Args:
        recipe_id (int): The ID of the recipe to update.
        recipe_data (Recipe): An object containing the updated user details.

    Returns:
        RecipeModel: The updated recipe record.

    Raises:
        DoesNotExist: If the recipe with the given ID does not exist.
    """
    recipe = RecipeModel.get_by_id(recipe_id)
    recipe.nameRecipe = recipe_data.nameRecipe
    recipe.descriptionRecipe = recipe_data.descriptionRecipe
    recipe.difficultyRecipe = recipe_data.difficultyRecipe
    recipe.timePreparation = recipe_data.timePreparation
    recipe.instructions = recipe_data.instructions
    recipe.nutritionalData = recipe_data.nutritionalData
    recipe.user_id = recipe_data.userId
    recipe.categoria_id = recipe_data.categoriaId
    recipe.save()
    return recipe


def delete_recipe_service(recipe_id: int):
    """
    Deletes a recipe from the database by their ID.

    Args:
        recipe_id (int): The ID of the recipe to delete.

    Returns:
        dict: A message confirming the deletion.

    Raises:
        DoesNotExist: If the recipe with the given ID does not exist.
    """
    recipe = RecipeModel.get_by_id(recipe_id)
    recipe.delete_instance()
    return {"message": "Recipe deleted successfully"}
