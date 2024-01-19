#!/usr/bin/python3
"""Module base.py"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Instance initialization
        Args:
            id: public instance attribute
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the json string representation of
        list_dictionaries(list of dictionaries)"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save JSON string of list_obj to a file"""
        objs = []
        if list_objs is not None:
            for o in list_objs:
                objs.append(cls.to_dictionary(o))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myFile:
            myFile.write(cls.to_json_string(objs))

    @staticmethod
    def from_json_string(json_string):
        """returns the JSON string representation of list"""
        if json_string is None or json_string == []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """this function returns all instances with
        all attributes set"""
        if cls.__name__ == "Square":
            dummy = cls(1)
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
