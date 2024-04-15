#!/usr/bin/python3
"""Console module"""


import cmd


class HBNBCmd(cmd.Cmd):
    """Console class for interactive shell"""

    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """exits the program"""
        return True

    def do_quit(self, arg):
        """ exits the shell """
        return True

if __name__ == "__main__":


    HBNBCmd().cmdloop()
