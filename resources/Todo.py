from flask_restful import Resource
from flask_restful import request
from db.todo import getById, update, delete

class ToDo(Resource):
    def get(self, id):        
        row = getById(id)
        if row:
            return row, 200
        else:
            return None, 404

    def delete(self, id):
        delete(id)
        return None, 204

    def put(self,id):        
        todoDict = request.get_json()
        todoDict['id'] = id
        update(todoDict)
        return None, 204