#!/usr/bin/python3
"""
Here you can find the class User
"""


from models.base_model import BaseModel


class User(BaseModel):
    """Here start the class user"""
    def __init__(self, *args, **kwargs):
        """Initializes user"""
        super().__init__.(*args, **kwargs)
