from flask import Flask, g
from flask_restful import Resource, Api, fields, marshal_with, request
from db.initialise import initDB
from db.conn import getDBConnection
from db.todo import add, getById, getAll, update, delete
import json
from resources.Todo import ToDo 
from resources.TodoList import ToDoList

app = Flask(__name__)
api = Api(app)

@app.before_request
def before_request():
    g.connection = getDBConnection()

@app.after_request
def after_request(response):
    g.connection.close()
    return response


initDB()

api.add_resource(ToDo, '/todo/<int:id>')
api.add_resource(ToDoList, '/todos/')

if __name__ == '__main__':
    app.run()