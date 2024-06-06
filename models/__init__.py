#!/usr/bin/python3

# import all Required classes
__all__ = ["BaseModel"]

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
