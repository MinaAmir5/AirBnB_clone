#!/usr/bin/python3
"""
User Defined Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Defined Place class"""
    name = ""
    user_id = ""
    city_id = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    longitude = 0.0
    latitude = 0.0
    amenity_ids = []
    description = ""
