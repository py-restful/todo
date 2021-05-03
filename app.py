from flask import Flask
from flask_restful import Resource, Api, fields, marshal_with, request

app = Flask(__name__)
api = Api(app)

todoListItems = [
    {
        'id': 1,
        'name': 'Task 1',
        'description': 'Task 1 description',
        'dueDate': '2021-05-22'
    },
    {
        'id': 2,
        'name': 'Task 2',
        'description': 'Task 3 description',
        'dueDate': '2021-05-23'
    },
    {
        'id': 3,
        'name': 'Task 3',
        'description': 'Task 3 description',
        'dueDate': '2021-05-24'
    }
]

class ToDo(Resource):
    def get(self, id):        
        todoItem = next(filter( lambda x: x['id'] == id, todoListItems), None)
        if todoItem:
            return todoItem, 200
        else:
            return None, 404
    def delete(self, id):
        global todoListItems
        todoListItems = list(filter(lambda x: x['id'] != id, todoListItems))
        return None, 204

    def put(self,id):        
        todoItem = next(filter( lambda x: x['id'] == id, todoListItems), None)
        if todoItem:
            todoDict = request.get_json()
            todoItem['name'] = todoDict['name']
            todoItem['description'] = todoDict['description']
            todoItem['dueDate'] = todoDict['dueDate']
            return todoItem, 200
        else:
            return None, 404

class ToDoList(Resource):
    def get(self):
        qs = request.args        
        return todoListItems

    def post(self):
        todoDict = request.get_json()
        todoDict['id'] = len(todoListItems) + 1
        todoListItems.append(todoDict)
        return todoDict    

api.add_resource(ToDo, '/todo/<int:id>')
api.add_resource(ToDoList, '/todos/')

app.run(port=5000, debug=True)