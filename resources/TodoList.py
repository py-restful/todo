from flask_restful import Resource
from flask_restful import request
from db.todo import add, getAll

class ToDoList(Resource):
    def get(self):
        return getAll()

    def post(self):
        todoDict = request.get_json()
        add(todoDict)        
        return None, 201