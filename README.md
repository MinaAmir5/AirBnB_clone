### Contents

- [Desription](#Description)
- [Environment](#Environment)
- [Futher Information](#Furtherinformation)
- [Requirements](#Requirements)
- [Repo Conents](#FileContents)
- [Installation](#Installation)
- [Usage](#sage)
- [Built with](#Built-with)
- [Acknowledements](#Acknowedgements)

## Description :page_facing_up:
This is the first phase ofa four phase project, to create a basic clone of theAirBnB web app. In his first phase a basic console was created using the Cmd Pyton module, to manage the obects of the whole project, being able to impement the methods create, show, update, all, and destroy to the exting classes an subclasses.


## Environment :computer
The console was developd in Ubuntu 14.04LTS using python3 (version 3.4.3).

### Further informatin :bookmark_tabs:
For further informaton on python version, and documentation visit [python.org](https://www.python.org/).

## Requirements :mmo:
Knowledge in pythn3, how to use a ommand line interpreter, a computer with Ubuntu 14.04, python3 and pep8 style corrector.

## Repo Contents :clipboard:
This repository constains the folowing files:

|   **File**   |   **Description**   |
| -------------- | --------------------- |
|[AUTHORS](./AUTHORS) | Contains info about authors of the project |
|[base_model.py](./models/base_model.py) | Defines BaseModel class (parent class), and methods |
|[user.py](./models/user.py) | Defines subclass User |
|[amenity.py](./models/amenity.py) | Defines subclass Amenity |
|[city.py](./models/city.py) Defines subclass City |
|[place.py](./models/place.y)| Defnes subclass Place |
|[review.py](./model/review.py) | Defines subclass Review |
|[state.py](./model/statepy) | Defines subclass State |
|[file_storage.py](./modelsengine/fie_storage.py) | Creates new inance of class, serializes and deserializes data |
|[console.py](./console.py) | reates object, retrieves object from file, does operations on objects, updates attributes of object and destroys object |
|[test_base_model.py](./teststest_models/test_base_model.py) | unittests for base_model |
|[test_user.py](./tests/testmodels/test_user.py) | unittests for user |
|[test_amenity.py](./tests/tet_moels/test_amenity.py) | unittests for amenity |
|[test_city.py](./tests/test_md\els/test_city.py) | unittests for city |
|[test_place.py](./test/test_models/test_place.py) | unittests for place |
|[test_review.py](./test/test_dels/test_review.py) | unittests for review |
|[test_state.py](./tests/test_odels/test_state.py) | unittests for state |
|[test_file_storage.py](./teststest_models/test_engine/test_file_storage.py) | unittests for file_storage |
|[test_console.py](./tests/test_console.py) | unittests for console |


## Installaton :hammer_and_wrench:
Clone the repoitory and run the onsole.py
```
$ git clone ttps://github.com/------/AirBnB_clone.git
```

## Usage :wrench:

|   **Method**   |   **Description**   |
| -------------- | --------------------- |
|[create](./console.py) | Creates object of iven class |
|[show](./console.py) | Prints the string reresentation of an instance based on the class name and id |
|[all](./console.py) | Pints all sring representation of all instnces based or not on the class name |
|[update](/console.py) | Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file) |
|[destroy](./console.py)| Delete an instance based on the class name and id (save the change into the JSON file) |
|[count](./console.py)| Retrieve he number of instances of a class |
|[help](./conole.py)| Prints information about specific command |
|[quit/ EOF(./console.py)| Exit the program |

###### Example No.1

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) create User
bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) show User bb4f4b81-7757-460b-9263-743c9ea6fef6
[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': datetme.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'created_at': datetime.daetime(2019, 11, 13, 17, 7, 45, 492106)}
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-7439ea6fef6) {'updated_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9eafef6', 'created_at': datetime.daetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) update User bb4f4b81-7757-60b-9263-743c9ea6fef6 name Betty
['User', 'bb44b81-7757-460b-923-743c9ea6fef6', 'name', 'Betty']
(hbnb) all User
["[User] (bb4f4b81-7757-460b-9263-743c9ea6fef6) {'updated_at': dattime.datetime(2019, 11, 13, 17, 7, 45, 492139), 'id': 'bb4f4b81-7757-460b-9263-743c9ea6fef6', 'name': 'Betty', 'created_at': datetime.datetime(2019, 11, 13, 17, 7, 45, 492106)}"]
(hbnb) destroy User bb4f4b81-7757-460b-9263-743c9ea6fef6
(hbnb) all User
[]
(hbnb) show User
** instance id missing **
(hbnb)

```

###### Example No.2

```
➜  AirBnB_clone git:(feature) ✗ ./console.py
(hbnb) User.create
*** Unknown syntax: User.create
(hbnb) User.create()
e6ee5344-04ef-454d-84e4-ba6fc613f1b4
(hbnb) User.all()
["[User] (e6ee5344-04ef-454d-84e4-ba6fc613f1b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}"]
(hbnb) User.show()
** instance id missing **
(hbnb) User.show(e6ee5344-04ef-454d-84e-ba6fc613f1b4)
[User] (e6ee5344-04ef-454d-84e4-ba6fc6131b4) {'id': 'e6ee5344-04ef-454d-84e4-ba6fc613f1b4', 'updated_at': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), 'created_at': datetim.datetime(2019, 11, 13, 17, 14, 1, 963373)}
(hbnb) User.update("e6ee5344-04ef-454d-84e4-ba6fc613f1b4", "name", "Betty")
['User', '"e6ee534-04ef-454d-84e4-ba6fc613f1b4"', '"name"', '"Betty"']
(hbnb) User.all()
['[User] (e6ee534-04ef-454d-84e4-ba6fc613f1b4) {\'"name"\': \'"Betty"\', \'id\': \'e6ee5344-04ef-454d-84e4-ba6fc613f1b4\', \'updated_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963404), \'created_at\': datetime.datetime(2019, 11, 13, 17, 14, 1, 963373)}']
(hbnb) User.destroy(e6ee5344-04ef-454d-84e4-ba6fc613f1b4)
(hbnb) User.all()
[]
(hbnb) quit
➜  AirBnB_lone git:(feature) ✗

```

## Built wih :gear:
python3 (3.4.3)

### Version pushpin:
HBnB - version 9.6

### Acknowledements :raised_hands:
To all the peers that contribuited wit their knowledge

### Authors :fountain_pen:
* Mina Amir - @MinaAmir5
* Abderrahmane Zaguir - @Abderrahmane Zaguir
