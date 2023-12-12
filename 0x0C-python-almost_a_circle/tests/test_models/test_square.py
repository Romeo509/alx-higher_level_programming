#!/usr/bin/python3
import unittest
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """Test cases for Square class"""

    def test_create_square(self):
        """Test creating an instance of Square"""
        s = Square(5)
        self.assertIsInstance(s, Square)

    def test_attributes(self):
        """Test Square attributes"""
        s = Square(3, 1, 2, 10)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_area_method(self):
        """Test area method of Square"""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display_method(self):
        """Test display method of Square"""
        s = Square(2)
        expected_output = "##\n##"
        with unittest.mock.patch(
           'sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_str_method(self):
        """Test str method of Square"""
        s = Square(4, 2, 1, 12)
        expected_str = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s), expected_str)

    def test_update_method(self):
        """Test update method of Square"""
        s = Square(5)
        s.update(89)
        self.assertEqual(s.id, 89)

    def test_to_dictionary_method(self):
        """Test to_dictionary method of Square"""
        s = Square(10, 2, 9, 12)
        expected_dict = {'x': 2, 'y': 9, 'id': 12, 'size': 10}
        self.assertEqual(s.to_dictionary(), expected_dict)

    # Add more test cases for Square class


if __name__ == '__main__':
    unittest.main()
