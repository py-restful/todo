from flask_restful import Resource
from flask_restful import request
from db.todo import add, getAll, getById

class ToDoList(Resource):
    def get(self):
        return getAll()

    def post(self):
        todoDict = request.get_json()
        affectedRowData = add(todoDict)        
        if affectedRowData.lastrowid > 0:
            return getById(affectedRowData.lastrowid), 201
        else:
            return {'error': 'ToDo item could not be created'}, 500