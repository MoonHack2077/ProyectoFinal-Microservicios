"""This module contains the service functions for the user class."""

from app.models.user_model import User
from app.config.database import User as UserModel
from app.services.role_service import get_all_roles_service
from app.services.family_service import get_all_families_service


def create_user_service(user: User):
    """
    Creates a new user in the database.

    Args:
        user (User): An object containing the user details.

    Returns:
        UserModel: The created user record.
    """
    
    # Obtener todos los roles disponibles
    available_roles = [role['idRole'] for role in get_all_roles_service()]
    avaliable_families = [family['idFamily'] for family in get_all_families_service()]
    
    # Validar el rol
    #if user.rolId not in available_roles:
     #   raise HTTPException(status_code=400, detail="Invalid role specified")
    
    # Crear el usuario
    user_record = UserModel.create(
        idUser=user.idUser,
        nameUser=user.nameUser,
        passwordUser=user.passwordUser,
        emailUser=user.emailUser,
        photoUser=user.photoUser,
        rolId_id =user.rolId,
        familyId_id = user.familyId
    )
    
    return user_record


def get_user_service(user_id: int):
    """
    Retrieves a user by their ID.

    Args:
        user_id (int): The unique identifier of the user.

    Returns:
        DICT: A dictionary containing the user's details.

    Raises:
        DoesNotExist: If the user with the given ID does not exist.
    """
    user = UserModel.get_by_id(user_id)
    return {
        "idUser": user.idUser,
        "nameUser": user.nameUser,
        "passwordUser": user.passwordUser,
        "emailUser": user.emailUser,
        "photoUser": user.photoUser,
        "role": user.rolId_id,
        "family": user.familyId_id
    }


def get_all_users_service():
    """
    Retrieves all users from the database.

    Returns:
        List: A list of dictionaries containing the data of each user's details.
    """
    users = list(UserModel.select())
    return [
        {
            "idUser": user.idUser,
            "nameUser": user.nameUser,
            "passwordUser": user.passwordUser,
            "emailUser": user.emailUser,
            "photoUser": user.photoUser,
            "role": user.rolId_id,
            "family": user.familyId_id
        }
        for user in users
    ]


def update_user_service(user_id: int, user_data: User):
    """
    Updates an existing user's details by their ID.

    Args:
        user_id (int): The ID of the customer to update.
        user_data (User): An object containing the updated user details.

    Returns:
        UserModel: The updated user record.

    Raises:
        DoesNotExist: If the user with the given ID does not exist.
    """
    user = UserModel.get_by_id(user_id)
    user.nameUser = user_data.nameUser
    user.passwordUser = user_data.passwordUser
    user.emailUser = user_data.emailUser
    user.photoUser = user_data.photoUser
    user.idRole_id = user_data.rolId
    user.familyId_id = user_data.familyId
    user.save()
    return user


def delete_user_service(user_id: int):
    """
    Deletes a user from the database by their ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: A message confirming the deletion.

    Raises:
        DoesNotExist: If the user with the given ID does not exist.
    """
    user = UserModel.get_by_id(user_id)
    user.delete_instance()
    return {"message": "User deleted successfully"}
