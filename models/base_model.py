#!/usr/bin/python3
''' A Python Module Representing AirBnB Clone '''

import uuid
from datetime import datetime
import models


class BaseModel:
    ''' Defines the BaseModel Class '''

    def __init__(self, *args, **kwargs):
        ''' Initializes the BaseModel Class '''

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "updated_at" or key == "created_at":
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        String representation of the BaseModel Class
        '''

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' Updates the public instance attribute '''
        self.updated_at = datetime.now()
        models.storage.save(self)

    def to_dict(self):
        '''
        Dictionary of all keys/values of __dict__ of the instance
        '''

        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
