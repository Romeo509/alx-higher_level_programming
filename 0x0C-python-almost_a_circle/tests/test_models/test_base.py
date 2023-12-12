#!/usr/bin/python3
"""Unittests for Base class"""
import unittest
from models.base import Base
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """Test cases for Base class"""

    def test_create_base(self):
        """Test creating an instance of Base"""
        b = Base()
        self.assertIsInstance(b, Base)

    def test_attributes(self):
        """Test Base attributes"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """Test assigning a custom id to Base"""
        b = Base(100)
        self.assertEqual(b.id, 100)

    def test_custom_id_after_default_ids(self):
        """Test assigning a custom id after default ids"""
        b1 = Base()
        b2 = Base(50)
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 50)
        self.assertEqual(b3.id, 2)

    def test_to_json_string(self):
        """Test to_json_string method of Base"""
        list_dicts = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        json_string = Base.to_json_string(list_dicts)
        self.assertIsInstance(json_string, str)

    def test_to_json_string_empty(self):
        """Test to_json_string method with an empty list"""
        empty_list = []
        json_string = Base.to_json_string(empty_list)
        self.assertEqual(json_string, "[]")

    def test_from_json_string(self):
        """Test from_json_string method of Base"""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertIsInstance(list_dicts, list)

    def test_from_json_string_empty(self):
        """Test from_json_string method with an empty string"""
        empty_string = ''
        list_dicts = Base.from_json_string(empty_string)
        self.assertEqual(list_dicts, [])

    # Add more test cases for Base class


if __name__ == '__main__':
    unittest.main()
