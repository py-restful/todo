from .queryrunner import QueryRunner

GET_ALL_TODOS = 'SELECT id, name, description, due FROM todo'
GET_TODO_BYID = 'SELECT id, name, description, due FROM todo WHERE id = :id'
INSERT_TODO   = 'INSERT INTO todo(name, description, due) VALUES (:name, :description, :due) RETURNING *'
#UPDATE_TODO   = 'UPDATE'

def add(todoItem):
    qr = QueryRunner()
    return qr.runDML(INSERT_TODO, **todoItem)

def getAll():
    qr = QueryRunner()
    return qr.runSelect(GET_ALL_TODOS)

def getById(id):
    qr = QueryRunner()
    rows = qr.runSelect(GET_TODO_BYID, id = id)
    ct = len(rows)
    return rows[0] if len(rows) > 0 else None
