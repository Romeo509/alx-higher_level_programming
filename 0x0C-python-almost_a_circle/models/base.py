#!/usr/bin/python3
import json


class Base:
    """Base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = cls.__name__ + ".json"
        obj_list = []
        if list_objs is not None:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        with open(filename, mode="w", encoding="utf-8") as file:
            file.write(cls.to_json_string(obj_list))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)  # Create a "dummy" Rectangle instance
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)  # Create a "dummy" Square instance
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                content = file.read()
                json_list = cls.from_json_string(content)
                return [cls.create(**obj) for obj in json_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to CSV file."""
        filename = cls.__name__ + ".csv"
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            if cls.__name__ == "Rectangle":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize CSV file to a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        instance = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    # ... rest of the class remains unchanged
