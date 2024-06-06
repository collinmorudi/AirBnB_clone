#!/usr/bin/python3

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """

    """
    __file_path = "file.json"
    __objects = {}

    def new(self, object):
        """
        """

        object_class_name = object.__class__.__name__
        key = f"{object_class_name}.{object.id}"

        FileStorage.__objects[key] = object

    def all(self):
        """
        """
        return FileStorage.__objects

    def save(self):
        """
        """

        all_objects = FileStorage.__objects
        object_dict = {}

        for object in all_objects.keys():
            object_dict[object] = all_objects[object].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    object_dict = json.load(file)
                    for key, value in object_dict.items():
                        class_name, object_id = key.split(".")

                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
