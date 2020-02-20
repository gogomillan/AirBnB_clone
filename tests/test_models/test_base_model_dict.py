#!/usr/bin/python3
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_mjson = my_model.to_dict()
print(my_mjson)
print("JSON of my_model:")
for key in my_mjson.keys():
    print("\t{}: ({}) - {}".format(key, type(my_mjson[key]), my_mjson[key]))

print("--")
my_new_model = BaseModel(**my_mjson)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))

print("--")
print(my_model is my_new_model)
