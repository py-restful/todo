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
        rows = update(todoDict)
        if len(rows) > 0:
            return rows[0], 200
        else:
            return None, 404