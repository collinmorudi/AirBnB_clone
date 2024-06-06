#!/usr/bin/python3

"""
User module - to represent user information such as name, email etc.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    class user that manages user information
    """
    first_name = ""
    last_name = ""
    email = ""
    password = ""
