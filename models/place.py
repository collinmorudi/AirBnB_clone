#!/usr/bin/python3
"""
Module - Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Public class attributes:
        name:                (str)
        city_id:             (str)
        user_id:             (str)
        description:         (str)
        number_rooms:        (int)
        number_bathrooms:    (int)
        max_guest:           (int)
        price_by_night:      (int)
        latitude:            (float)
        longitude:           (float)
        amenity_ids:         (list)
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
