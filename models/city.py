#!/usr/bin/python3
"""
Module - City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Public class attributes:
        name:     (str)
        state_id: (str)
    """
    name = ""
    state_id = ""
