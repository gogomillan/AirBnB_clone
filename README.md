# AirBnB Clone - The Console
the first segment of the AirBnB project at Holberton School is the console in this project we are going to share all our knowledge about higher level programming. The goal is to eventually deploy our server a simple copy of AirBnB. A command interpreter is created in this segment to manage objects.

#### Functionalities of this command interpreter:
* Create a new object (ex: a new User or a new Amenity)
* Retrieve an object from a file, a database etc...
* Do operations on objects
* Update attributes of an object
* Destroy an object

## Table of Content
* [Environment](#environment)
* [Installation](#installation)
* [File Descriptions](#file-descriptions)
* [Usage](#usage)
* [Examples of use](#examples-of-use)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Environment
This project is interpreted/tested on Ubuntu 14.04 LTS using python3 (version 3.4.3)

## Installation
* Clone this repository: `git clone "https://github.com/daod2003/AirBnB_clone"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

## File Descriptions
[console.py](console.py) - the console contains the command interpreter. 
List of commands that the console supports:
* `EOF` - ext the console
* `quit` - ext the console
* `<emptyline>` - overwrites default emptyline method
* `create` - Creates a new instance of`BaseModel`, saves it in a JSON file and prints the id
* `destroy` - Deletes an instance based on the class name and id save the change into the JSON file. 
* `show` - Prints the string of an instance based on the class name and id.
* `all` - Prints all string of all instances based or not on the class name. 
* `update` - Updates an instance based on the class name and id by adding or updating attribute save the change into the JSON file.

#### `models/` directory contains classes used for this project:
[base_model.py](/models/base_model.py) - The BaseModel class
* `def __init__(self, *args, **kwargs)` - Start the base model
* `def __str__(self)` - String representation of the BaseModel class
* `def save(self)` - Updates the attribute `updated_at` with the current datetime
* `def to_dict(self)` - returns a dictionary containing all keys/values of the instance

Classes inherited from Base Model:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

#### `/models/engine` directory contains File Storage class that handles JSON serialization and deserialization :
[file_storage.py](/models/engine/file_storage.py) - serializes instances to a JSON file & deserializes back to instances
* `def all(self)` - returns the dictionary __objects
* `def new(self, obj)` - sets in __objects the obj with key <obj class name>.id
* `def save(self)` - serializes __objects to the JSON file (path: __file_path)
* ` def reload(self)` -  deserializes the JSON file to __objects

#### `/tests` directory contains all unit test cases for this project:
[/test_models/test_base_model.py](/tests/test_models/test_base_model.py) - Contains the TestBaseModel
[/test_models/test_amenity.py](/tests/test_models/test_amenity.py) - Contains the TestAmenity class
[/test_models/test_city.py](/tests/test_models/test_city.py) - Contains the TestCityD class
[/test_models/test_file_storage.py](/tests/test_models/test_file_storage.py) - Contains the TestFileStorage class
[/test_models/test_place.py](/tests/test_models/test_place.py) - Contains the TestPlace class
[/test_models/test_review.py](/tests/test_models/test_review.py) - Contains the TestReview class
[/test_models/state.py](/tests/test_models/test_state.py) - Contains the TestState class
[/test_models/user.py](/tests/test_models/test_user.py) - Contains the TestUser class

## Examples of use
```
vagrant@vagrant-ubuntu-trusty-64:~/AirBnB_clone$ ./console.py 
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) all MyModel
** class doesn't exist **
(hbnb) create BaseModel
b342bd3a-5c20-4ec3-823a-106df91c66c6
(hbnb) all BaseModel
["[BaseModel] (b342bd3a-5c20-4ec3-823a-106df91c66c6) {'updated_at': datetime.datetime(2020, 2, 20, 4, 42, 33, 230066), 'id': 'b342bd3a-5c20-4ec3-823a-106df91c66c6', 'created_at': datetime.datetime(2020, 2, 20, 4, 42, 33, 229540)}"]
(hbnb) Show BaseModel
*** Unknown syntax: Show BaseModel
(hbnb) show BaseModel b342bd3a-5c20-4ec3-823a-106df91c66c6
[BaseModel] (b342bd3a-5c20-4ec3-823a-106df91c66c6) {'updated_at': datetime.datetime(2020, 2, 20, 4, 42, 33, 230066), 'id': 'b342bd3a-5c20-4ec3-823a-106df91c66c6', 'created_at': datetime.datetime(2020, 2, 20, 4, 42, 33, 229540)}
(hbnb) destroy BaseModel b342bd3a-5c20-4ec3-823a-106df91c66c6
(hbnb) Show BaseModel b342bd3a-5c20-4ec3-823a-106df91c66c6
*** Unknown syntax: Show BaseModel b342bd3a-5c20-4ec3-823a-106df91c66c6
(hbnb) show BaseModel b342bd3a-5c20-4ec3-823a-106df91c66c6
** no instance found **
(hbnb) quit
```

## Bugs
No known bugs at this time.

## Authors
Gonzalo Gomez - [Github](https://github.com/gogomillan)
David Ortiz - [Github](https://github.com/daod2003)

## Lincense
[LICENSE](LICENSE) - Public Domain. No copy write protection. 
