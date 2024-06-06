#!/usr/bin/python3
"""Console module"""


import cmd


class HBNBCommand(cmd.Cmd):
    """Console class for interactive shell"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Exit on Ctrl+D"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
