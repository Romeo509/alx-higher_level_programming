#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle class"""

    def test_create_rectangle(self):
        """Test creating an instance of Rectangle"""
        r = Rectangle(3, 4)
        self.assertIsInstance(r, Rectangle)

    def test_attributes(self):
        """Test Rectangle attributes"""
        r = Rectangle(3, 4, 1, 2, 10)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 10)

    def test_area_method(self):
        """Test area method of Rectangle"""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_display_method(self):
        """Test display method of Rectangle"""
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##"

        with unittest.mock.patch(
          'sys.stdout', new_callable=io.StringIO) as mock_stdout:

            r.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str_method(self):
        """Test str method of Rectangle"""
        r = Rectangle(4, 6, 2, 1, 12)
        expected_str = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected_str)

    def test_update_method(self):
        """Test update method of Rectangle"""
        r = Rectangle(5, 7)
        r.update(89)
        self.assertEqual(r.id, 89)

    def test_to_dictionary_method(self):
        """Test to_dictionary method of Rectangle"""
        r = Rectangle(10, 2, 3, 4, 12)
        expected_dict = {'x': 3, 'y': 4, 'id': 12, 'width': 10, 'height': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)

    # Add more test cases for Rectangle class


if __name__ == '__main__':
    unittest.main()
