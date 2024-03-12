#!/usr/bin/python3
''' A Python Module Representing the Console '''

import cmd


class HBNBCommand(cmd.Cmd):
    ''' Defines the command interpreter class '''

    prompt = "(hbnb) "

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
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
