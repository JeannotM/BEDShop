import sqlite3
import os

class CategoryModel:
    
    def __init__(self, id, name):
        """CategoryModel constructor

        Args:
            id (int): database id
            name (string): display name
        """
        self.id = id
        self.name = name
    
    @classmethod
    def find_all(cls):
        """returns all categories in the database

        Returns:
            list: all categories
        """

        # Categories should be fetched from the database! 
        # This is just an example to make it work.

        # Create an empty list
        categories = list()
        # Create a new category
        category_1 = CategoryModel(1, 'bedden')
        # Add the new category to the list
        categories.append(category_1)

        # return the list of categories
        return categories
    
    def json(self):
        """Returns a JSON version of the current object

        Returns:
            dict: the object
        """
        return self.__dict__
        
