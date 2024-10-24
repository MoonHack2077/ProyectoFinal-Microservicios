"""This module contains the service functions for the pantry class."""

from app.models.pantry_model import Pantry
from app.config.database import Pantry as PantryModel


def create_pantry_service(pantry: Pantry):
    """
    Creates a new pantry in the database.

    Args:
        pantry (Pantry): An object containing the pantry details.

    Returns:
        PantryModel: The created pantry record.
    """
    pantry_record = PantryModel.create(
        idPantry=pantry.idPantry,
        user_id=pantry.user_id
        )
    return pantry_record


def get_pantry_service(pantry_id: int):
    """
    Retrieves a pantry by its ID.

    Args:
        pantry_id (int): The unique identifier of the pantry.

    Returns:
        DICT: A dictionary containing the pantry's details.

    Raises:
        DoesNotExist: If the pantry with the given ID does not exist.
    """
    pantry = PantryModel.get_by_id(pantry_id)
    return {"id": pantry.idPantry,
            "user_id": pantry.user_id}


def get_all_pantries_service():
    """
    Retrieves all pantries from the database.

    Returns:
        List: A list of dictionaries containing the data of each pantry's details.
    """
    pantries = list(PantryModel.select())
    return [{"id": pantry.idPantry,
             "user_id": pantry.user_id} for pantry in pantries]


def update_pantry_service(pantry_id: int, pantry_data: Pantry):
    """
    Updates an existing pantry's details by its ID.

    Args:
        pantry_id (int): The ID of the pantry to update.
        pantry_data (Pantry): An object containing the updated pantry details.

    Returns:
        PantryModel: The updated pantry record.

    Raises:
        DoesNotExist: If the pantry with the given ID does not exist.
    """
    pantry = PantryModel.get_by_id(pantry_id)
    pantry.user_id = pantry_data.user_id
    pantry.save()
    return pantry


def delete_pantry_service(pantry_id: int):
    """
    Deletes a pantry from the database by its ID.

    Args:
        pantry_id (int): The ID of the pantry to delete.

    Returns:
        dict: A message confirming the deletion.

    Raises:
        DoesNotExist: If the pantry with the given ID does not exist.
    """
    pantry = PantryModel.get_by_id(pantry_id)
    pantry.delete_instance()
    return {"message": "Pantry deleted successfully"}
