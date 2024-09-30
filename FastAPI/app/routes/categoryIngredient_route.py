"""
This module contains the routes for managing categoryIngredient data.
"""
from fastapi import APIRouter, Body, HTTPException
from app.models.categoryIngredient_model import CategoryIngredient
from peewee import DoesNotExist
from app.services.categoryIngredient_service import (
    create_category_ingredient_service,
    get_all_category_ingredients_service,
    get_category_ingredient_service,
    update_category_ingredient_service,
    delete_category_ingredient_service
)

category_ingredient_router = APIRouter()

@category_ingredient_router.post("/")
def create_category_ingredient(categoryIngredient: CategoryIngredient = Body(...)):
    """
    Creates a new categoryIngredient in the database.

    Parameters:
        categoryIngredient (CategoryIngredient): An object containing the categoryIngredient details.
        
    Returns:
        The created categoryIngredient object.
    """
    return create_category_ingredient_service(categoryIngredient)

@category_ingredient_router.get("/{category_ingredient_id}")
def read_category_ingredient(category_ingredient_id: int):
    """
    Retrieves a categoryIngredient by its ID.

    Args:
        category_ingredient_id (int): The ID of the categoryIngredient to retrieve.

    Returns:
        CategoryIngredient: The categoryIngredient object.

    Raises:
        HTTPException: If the categoryIngredient is not found.
    """
    try:
        return get_category_ingredient_service(category_ingredient_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryIngredient not found") from exc

@category_ingredient_router.get("/")
def read_category_ingredients():
    """
    Reads and returns all categoryIngredients.

    Returns:
        List[CategoryIngredient]: A list of all categoryIngredients.
    """
    return get_all_category_ingredients_service()

@category_ingredient_router.put("/{category_ingredient_id}")
def update_category_ingredient(category_ingredient_id: int, category_ingredient_data: CategoryIngredient = Body(...)):
    """
    Update a categoryIngredient with the given category_ingredient_id and category_ingredient_data.

    Parameters:
        category_ingredient_id (int): The ID of the categoryIngredient to update.
        category_ingredient_data (CategoryIngredient): The updated categoryIngredient data.

    Returns:
        The updated categoryIngredient object.

    Raises:
        HTTPException: If the categoryIngredient with the given ID does not exist.
    """
    try:
        return update_category_ingredient_service(category_ingredient_id, category_ingredient_data)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryIngredient not found") from exc

@category_ingredient_router.delete("/{category_ingredient_id}")
def delete_category_ingredient(category_ingredient_id: int):
    """
    Delete a categoryIngredient with the given category_ingredient_id.

    Args:
        category_ingredient_id (int): The ID of the categoryIngredient to be deleted.

    Returns:
        None

    Raises:
        HTTPException: If the categoryIngredient does not exist.
    """
    try:
        return delete_category_ingredient_service(category_ingredient_id)
    except DoesNotExist as exc:
        raise HTTPException(status_code=404, detail="CategoryIngredient not found") from exc