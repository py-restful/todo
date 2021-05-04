### ToDo API
This is POC for REST api built using flask / flaskRESTful

This restful service exposes a set of endpoints to manage ToDo item list. Each todo item has the following properties
1. name: Name for the ToDo item (ex - Buy Groceries)
2. description: Additiona description(ex - Buy groceries from super mart)
3. due: Due date for the todo item (ex - "2021-05-05")

The endpoints and requests are described below

### Endpoints
The `main` branch is deployed to Heroku https://todo-py-flask-rest.herokuapp.com/. The details of endpoints and requests are listed below.

##### Create a new todo item - POST /todos

```
curl -X POST -d '{"name":"T1", "description":"Test description", "due":"2021-05-10"}'  -H 'Content-Type: application/json' https://todo-py-flask-rest.herokuapp.com/todos/
```

##### Update todo item - PUT /todo/:id

```
curl -X PUT -d '{"name":"T1", "description":"Test description updated", "due":"2021-05-20"}'  -H 'Content-Type: application/json' https://todo-py-flask-rest.herokuapp.com/todo/<id>
```


##### Delete todo item - DELETE /todo/:id

```
curl -X DELETE   -H 'Content-Type: application/json' https://todo-py-flask-rest.herokuapp.com/todo/<id>
```

##### Get todo item by ID - GET /todo/:id

```
curl -X GET  -H 'Content-Type: application/json' https://todo-py-flask-rest.herokuapp.com/todo/<id>
```

##### Get all todo items - GET /todos/

```
curl -X GET  -H 'Content-Type: application/json' https://todo-py-flask-rest.herokuapp.com/todos/
```

### Frameworks / tools used
* Python 3.9.4
* flaskRESTful 0.3.8
* sqlite3
* uWSGI 2.0.19.1

### Steps to Run locally
1. Create a virtual environment with Python 3.9.4
2. Activate the virtual environment
3. In terminal / command line run `pip install -r requirements.txt` from repo folder
4. Run `flask run`
