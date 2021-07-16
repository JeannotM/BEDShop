from models.category import CategoryModel
from flask import request
from flask_restful import Resource
import os

class Categories(Resource):
    
    def get(self):
        """return all categories

        Returns:
            dict: containing all categories
        """
        categories = CategoryModel.find_all()
        if categories:
            return {'categories': [category.json() for category in categories]}, 200
        return {'message': 'No categories found'}, 404
