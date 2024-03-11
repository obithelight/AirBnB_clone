#!/usr/bin/python3
''' A Python Module Representing AirBnB Clone '''

import uuid
from datetime import datetime


class BaseModel:
    ''' Defines the BaseModel Class '''

    def __init__(self):
        ''' Initializes the BaseModel class '''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        '''
        Returns an informal string representation of the BaseModel Class
        '''
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        ''' Updates the public instance attribute '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Returns a dictionary of all keys/values of __dict__ of the instance
        '''
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = self.__class__.__name__
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
