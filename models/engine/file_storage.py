#!/usr/bin/python3
""" This module creates the FileStorage class """

import json


class FileStorage:
    ''' This serializes instances to a JSON file and deserializes
       JSON file back to instances
    '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' returns the dict __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in `__objects` the `obj` with key `<obj class name>.id` '''

        name = obj.__class__.__name__
        key = f"{name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' serializes `__objects` to the JSON file '''

        with open(self.__file_path, "w", encoding="utf-8") as file:
            dict_choice = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_choice, file)

    def reload(self):
        ''' deserializes the JSON file to __objects '''

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path, "r", encoding="utf-8") as file:
                obj_dict = json.load(file)
                for value in obj_dict.values():
                    cls_name = value["__class__"]
                    #del o["__class__"]
                    self.new(eval(cls_name)(**value))

        except FileNotFoundError:
            pass
