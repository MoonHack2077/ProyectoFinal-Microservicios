"""This module contains the service functions for the categoryIngredient class."""
from app.models.categoryIngredient_model import CategoryIngredient

def create_category_ingredient_service(categoryIngredient):
    """
    Creates a new categoryIngredient in the database.

    Args:
        categoryIngredient (CategoryIngredient): An object containing the categoryIngredient details.
        
    Returns:
        CategoryIngredientModel: The created categoryIngredient record.
    """
    category_ingredient_record = CategoryIngredient.create(
        idCategoryIngredient=categoryIngredient.idCategoryIngredient,
        nameCategoryIngredient=categoryIngredient.nameCategoryIngredient,
        descriptionCategoryIngredient=categoryIngredient.descriptionCategoryIngredient
    )
    return category_ingredient_record

def get_category_ingredient_service(category_ingredient_id: int):
    """
    Retrieves a categoryIngredient by its ID.

    Args:
        category_ingredient_id (int): The unique identifier of the categoryIngredient.

    Returns:
        DICT: A dictionary containing the categoryIngredient's details.
        
    Raises:
        DoesNotExist: If the categoryIngredient with the given ID does not exist.
    """
    category_ingredient = CategoryIngredient.get_by_id(category_ingredient_id)
    return {
        "id": category_ingredient.idCategoryIngredient,
        "name": category_ingredient.nameCategoryIngredient,
        "description": category_ingredient.descriptionCategoryIngredient
    }

def get_all_category_ingredients_service():
    """
    Retrieves all categoryIngredients from the database.

    Returns:
        List: A list of dictionaries containing the data of each categoryIngredient's details.
    """
    category_ingredients = list(CategoryIngredient.select())
    return [
        {
        "id": category_ingredient.idCategoryIngredient,
        "name": category_ingredient.nameCategoryIngredient,
        "description": category_ingredient.descriptionCategoryIngredient
        }
        for category_ingredient in category_ingredients
    ]

def update_category_ingredient_service(category_ingredient_id: int, category_ingredient_data: CategoryIngredient):
    """
    Updates an existing categoryIngredient's details by its ID.

    Args:
        category_ingredient_id (int): The ID of the categoryIngredient to update.
        category_ingredient_data (CategoryIngredient): An object containing the updated categoryIngredient details.
        
    Returns:
        CategoryIngredientModel: The updated categoryIngredient record.
        
    Raises:
        DoesNotExist: If the categoryIngredient with the given ID does not exist.
    """
    category_ingredient = CategoryIngredient.get_by_id(category_ingredient_id)
    category_ingredient.nameCategoryIngredient = category_ingredient_data.nameCategoryIngredient,
    category_ingredient.descriptionCategoryIngredient = category_ingredient_data.descriptionCategoryIngredient
    category_ingredient.save()
    return category_ingredient

def delete_category_ingredient_service(category_ingredient_id: int):
    """
    Deletes a categoryIngredient from the database by its ID.

    Args:
        category_ingredient_id (int): The ID of the categoryIngredient to delete.
        
    Returns:
        dict: A message confirming the deletion.
        
    Raises:
        DoesNotExist: If the categoryIngredient with the given ID does not exist.
    """
    category_ingredient = CategoryIngredient.get_by_id(category_ingredient_id)
    category_ingredient.delete_instance()
    return {"message": "CategoryIngredient deleted successfully"}