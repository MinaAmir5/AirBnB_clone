#!/usr/bin/python3
"""
User defined review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """User reviews for a place"""
    place_id = ""
    user_id = ""
    text = ""
