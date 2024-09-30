"""
This module contains the Pydantic model for notification data.
"""
from pydantic import BaseModel
from datetime import date

class Notification(BaseModel):
    """
    Notification model class.
    Attributes:
        idNotification (int): The unique identifier of the notification.
        message (str): The message of the notification.
        dateNotification (date): The date of the notification.
    """
    idNotification : int
    message : str
    dateNotification : date