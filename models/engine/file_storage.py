#!/usr/bin/python3
''' A Python Module Representing BaseModel '''

import json

class FileStorage:
    ''' Defines the FileStorage Class '''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        ''' public instance method '''
        return self.__objects

    def new(self, obj):
        ''' public instance method '''

        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        ''' public instance method '''

        with open(self.__file_path, "w", encoding="utf-8") as f:
            d = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(d, f)

    def reload(self):
        ''' deserializes the JSON file to __objects '''

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                for o in obj_dict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))

        except FileNotFoundError:
            return
