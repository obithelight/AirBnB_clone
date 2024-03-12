#!/usr/bin/python3
''' A Python Module Representing the Console '''

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    ''' Defines the command interpreter class '''

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        '''Quits command to exit the program
        '''
        return True

    def do_EOF(self, arg):
        '''EOF signal to exit the program
        '''
        return True

    def emptyline(self):
        ''' Allows an empty line to do nothing
        '''
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel
        '''
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()
            print(new_object.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
