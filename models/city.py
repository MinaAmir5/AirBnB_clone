#!/usr/bin/python3
"""
Defines city class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """class defines a city to look for"""
    state_id = ""
    name = ""
