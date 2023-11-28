#!/usr/bin/python3
"""Module containing the say_my_name function.
"""

def say_my_name(first_name, last_name=""):
    """Prints a message with the provided first and last names.

    Args:
        first_name (str): The first name.
        last_name (str, optional): The last name. Defaults to "".

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Walter")
        My name is Walter
        >>> say_my_name("Bob")
        My name is Bob
        >>> say_my_name(12, "White")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string")

    full_name = f"{first_name} {last_name}" if last_name else first_name
    print(f"My name is {full_name}")

if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter")
    say_my_name("Bob")

    try:
        say_my_name(12, "White")
    except TypeError as e:
        print(e)
