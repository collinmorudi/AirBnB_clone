#!/usr/bin/python3
"""Console module"""


import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.place import Place
from models.review import Review
from models.city import City
from models.amenity import Amenity
import shlex


class HBNBCommand(cmd.Cmd):
    """Console class for interactive shell"""

    classes = {"BaseModel", "User", "Amenity", "State",
                            "City", "Place", "Review"}
    prompt = "(hbnb) "

    def parse_args(self, arg):
        """Parse command line arguments"""
        args = arg.split()  # split on spaces
        return args

    def do_EOF(self, arg):
        """Exit on Ctrl+D"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        args = self.parse_args(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            # create a new instance
            instance = eval(f"{args[0]}")()

            # save a new instcance
            instance.save()

            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id.
        """
        args = self.parse_args(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the
        change into the JSON file)
        """
        args = self.parse_args(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"

            # delete the object based on key
            if key in objects:
                del objects[key]
                # save changes
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not
        on the class name
        """

        args = self.parse_args(arg)

        # get all objects
        objects = storage.all()

        if len(args) == 0:
            for key, value in objects.items():
                print(str(value))
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split(".")[0] == args[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file)
        """
        args = self.parse_args(arg)

        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = f"{args[0]}.{args[1]}"

            if key not in objects:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attribute_name = args[2]
                attribute_value = args[3]

                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass

                setattr(obj, attribute_name, attribute_value)
                obj.save()

    def default(self, arg):
        """
        default mfunction to handle syntax errors
        """
        # default method calls
        default_commands = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "update": self.do_update,
                "count": self.do_count
                }

        # get class name
        args = arg.split(".")
        class_name = args[0]

        # get command
        command = args[1].split("(")[0]
        first_arg = args[1].split("(")
        object_id = first_arg[1].split(")")[0].strip('"').strip("'")

        if command in default_commands.keys():
            return default_commands[command](f"{class_name} {object_id}")

        print(f"** unknown syntax ** {arg}")

    def do_count(self, arg):
        """
        Count the number of instances of a class passed as arg
        """
        objects = storage.all()

        args = shlex.split(arg)

        class_name = args[0]

        if class_name in HBNBCommand.classes:
            count = 0
            for obj in objects.values():
                if obj.__class__.__name__ == class_name:
                    count += 1
            print(count)
        else:
            print("** class doens't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
