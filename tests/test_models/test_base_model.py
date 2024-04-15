#!/usr/bin/python3
"""
Test BaseModel
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    """

    def test_init(self):
        model_obj = BaseModel()
        self.assertIsNotNone(model_obj.id)
        self.assertIsNotNone(model_obj.created_at)
        self.assertIsNotNone(model_obj.updated_at)

    def test_save(self):
        model_obj = BaseModel()
        init_updated_at = model_obj.updated_at
        new_updated_at = model_obj.save()
        self.assertNotEqual(init_updated_at, new_updated_at)

    def test_to_dict(self):
        model_obj = BaseModel()
        self.assertTrue(isinstance(model_obj.to_dict(), dict))
        
        model_dict = model_obj.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["id"], model_obj.id)
        self.assertEqual(model_dict["created_at"], model_obj.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], model_obj.updated_at.isoformat())


    def test_str(self):
        model_obj = BaseModel()
        self.assertTrue(str(model_obj).startswith("[BaseModel]"))
        self.assertIn(str(model_obj.__dict__), str(model_obj))
        self.assertIn(model_obj.id, str(model_obj))

    
if __name__ == "__main__":
    unittest.main()
