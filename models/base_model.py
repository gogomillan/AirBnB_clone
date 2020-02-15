#!/usr/bin/python3
"""
Here you can find the base model function
"""

import models
import uuid
from datetime import datetime

#time = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """Here start the BaseModel function"""
    def __init__(self):
        """ here init the function """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = self.create_at

    def __str__(self):
        """Function that prints class name, id and __dic"""
        print("[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                        self.__dict__))

    def save(self):
        """Function that updates the public instance attribute
updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all keys/values of dict
 of the instance """
        new_dict = self.__dict__.copy()
        if "created_at" in __dict__:
            new_dict["created_at"] = new_dict["created_at"].isoformat()
        if "updated_at" in self.__dict__:
            new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
