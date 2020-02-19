#!/usr/bin/python3
"""
Here you can find the FileStorage Class
"""

import json
from models.base_model import BaseModel
from models.user import User

classes = {"BaseModel": BaseModel, "User": User}


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

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path)"""
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                js = json.load(f)
            for key in js:
                self.__objects[key] = classes[js[key]["__class__"]](**js[key])
        except:
            pass
