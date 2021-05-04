from flask_restful import Resource
from flask_restful import request
from db.todo import getById, update, delete

class ToDo(Resource):
    def get(self, id):        
        row = getById(id)
        if row:
            return row, 200
        else:
            return {'error': 'Todo item is not available in database'}, 404

    def delete(self, id):
        delete(id)
        return None, 204

    def put(self,id):        
        todoDict = request.get_json()
        todoDict['id'] = id
        affectedRowData = update(todoDict)
        if affectedRowData.rowcount > 0:
            return getById(id), 200
        else:
            return {'error': 'Todo item could not be updated'}, 500