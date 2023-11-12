#!/usr/bin/python3
"""
Class that serilizes insances to a JSON file
and deserialies JSON fie to intances
"""
import os
import json


class FileStorage:
    """ Class that serialzes and deerializes JSON ojects """
    __objects = {}
    __file_path = "file.json"

    def save(self):
        """ Serializes __objcts to the JSON fle """
        dictionary = {}

        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dictionary, f)

    def new(self, obj):
        """ Sets in __objects te obj with key <obj clas name >.id """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def reload(self):
        """ Deserialies __objcts from the JSON fle """
        from models.city import City
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.state import State
        from models.base_model import BaseModel
        from models.review import Review
        dct = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'City': City, 'Amenity': Amenity, 'State': State,
               'Review': Review}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as f:
                for key, value in json.load(f).items():
                    self.new(dct[value['__class__']](**value))

    def all(self):
        """ Retuns the ditionary __objects """
        return FileStorage.__objects
