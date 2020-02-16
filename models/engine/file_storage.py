#!/usr/bin/python3
"""
Here you can find the FileStorage Class
"""

import json
from model.base_model import BaseModel

class FileStorage:
    """that serializes instances to a JSON file and deserializes
JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
