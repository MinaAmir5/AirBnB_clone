#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for user creation"""
    first_name = ""
    last_name = ""
    email = ""
    password = ""
