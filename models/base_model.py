#!/usr/bin/python3
"""
Here you can find the base model function
"""

import models
import uuid
from datetime import datetime

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """Here start the BaseModel function"""
    def __init__(self):
        """ here init the function """
        self.id = str(uuid.uuid4())
        self.create_at = datetime.now()
        self.update_at = self.create_at

    def __str__(self):
        """ Function that prints class name, id and __dic """
        pass

    def save(self):
        """ Function that updates the public instance attribute
updated_at with the current datetime """
        pass

    def to_dict(self):
        """ returns a dictionary containing all keys/values of dict
 of the instance """
        pass
