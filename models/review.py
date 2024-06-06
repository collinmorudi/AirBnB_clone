#!/usr/bin/python3
"""
Module - Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Public class attributes:
        place_id:            (str)
        user_id:             (str)
        text:                (str)
    """
    place_id = ""
    user_id = ""
    text = ""
