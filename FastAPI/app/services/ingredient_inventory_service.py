"""This module contains the service functions for the ingredientInventory class."""

from app.models.ingredient_inventory_model import IngredientInventory
from app.config.database import IngredientInventory as IngredientInventoryModel


def create_ingredient_inventory_service(ingredient_inventory: IngredientInventory):
    """
    Creates a new ingredientInventory in the database.

    Args:
        ingredient_inventory (IngredientInventory): An object containing the ingredient details.

    Returns:
        IngredientInventoryModel: The created ingredientInventory record.
    """
    ingredient_inventory_record = IngredientInventoryModel.create(
        ingredientId=ingredient_inventory.ingredientId,
        nameIngredient=ingredient_inventory.nameIngredient,
        amountIngredient=ingredient_inventory.amountIngredient,
        unitIngredient=ingredient_inventory.unitIngredient,
        dateExpirationIngredient=ingredient_inventory.dateExpirationIngredient,
        pantry_id = ingredient_inventory.pantry_id
    )
    return ingredient_inventory_record


def get_ingredient_inventory_service(ingredient_inventory_id: int):
    """
    Retrieves an ingredientInventory by its ID.

    Args:
        ingredient_inventory_id (int): The unique identifier of the ingredientInventory.

    Returns:
        DICT: A dictionary containing the ingredientInventory's details.

    Raises:
        DoesNotExist: If the ingredientInventory with the given ID does not exist.
    """
    ingredient_inventory = IngredientInventoryModel.get_by_id(ingredient_inventory_id)
    return {
        "ingredientId": ingredient_inventory.ingredientId,
        "nameIngredient": ingredient_inventory.nameIngredient,
        "amountIngredient": ingredient_inventory.amountIngredient,
        "unitIngredient": ingredient_inventory.unitIngredient,
        "dateExpirationIngredient": ingredient_inventory.dateExpirationIngredient,
        "pantry_id": ingredient_inventory.pantry_id
    }


def get_all_ingredient_inventories_service():
    """
    Retrieves all ingredientInventories from the database.

    Returns:
        List: A list of dictionaries containing the data of each ingredientInventory's details.
    """
    ingredient_inventories = list(IngredientInventoryModel.select())
    return [
        {
            "id": ingredient_inventory.ingredientId,
            "nameIngredient": ingredient_inventory.nameIngredient,
            "amountIngredient": ingredient_inventory.amountIngredient,
            "unitIngredient": ingredient_inventory.unitIngredient,
            "dateExpirationIngredient": ingredient_inventory.dateExpirationIngredient,
            "pantry_id": ingredient_inventory.pantry_id
        }
        for ingredient_inventory in ingredient_inventories
    ]


def update_ingredient_inventory_service(
    ingredient_inventory_id: int, ingredient_inventory_data: IngredientInventory
):
    """
    Updates an existing ingredientInventory's details by its ID.

    Args:
        ingredient_inventory_id (int): The ID of the ingredientInventory to update.
        ingredient_inventory_data (IngredientInventory): An object containing the
        updated ingredientInventory details.

    Returns:
        IngredientInventoryModel: The updated ingredientInventory record.

    Raises:
        DoesNotExist: If the ingredientInventory with the given ID does not exist.
    """
    ingredient_inventory = IngredientInventoryModel.get_by_id(ingredient_inventory_id)
    ingredient_inventory.nameIngredient = ingredient_inventory_data.nameIngredient
    ingredient_inventory.amountIngredient = ingredient_inventory_data.amountIngredient
    ingredient_inventory.unitIngredient = ingredient_inventory_data.unitIngredient
    ingredient_inventory.dateExpirationIngredient = ingredient_inventory_data.dateExpirationIngredient
    ingredient_inventory.pantry_id = ingredient_inventory_data.pantry_id
    ingredient_inventory.save()
    return ingredient_inventory


def delete_ingredient_inventory_service(ingredient_inventory_id: int):
    """
    Deletes an ingredientInventory from the database by its ID.

    Args:
        ingredient_inventory_id (int): The ID of the ingredientInventory to delete.

    Returns:
        dict: A message confirming the deletion.

    Raises:
        DoesNotExist: If the ingredientInventory with the given ID does not exist.
    """
    ingredient_inventory = IngredientInventoryModel.get_by_id(ingredient_inventory_id)
    ingredient_inventory.delete_instance()
    return {"message": "IngredientInventory deleted successfully"}
