from .queryrunner import QueryRunner

GET_ALL_TODOS = 'SELECT id, name, description, due FROM todo'
GET_TODO_BYID = 'SELECT id, name, description, due FROM todo WHERE id = :id'
#INSERT_TODO   = 'INSERT INTO todo(name, description, due) VALUES (:name, :description, :due) RETURNING *'
#UPDATE_TODO   = 'UPDATE todo SET name=:name, description=:description, due=:due WHERE id=:id RETURNING *'
#DELETE_TODO   = 'DELETE FROM todo WHERE id=:id RETURNING *'
INSERT_TODO   = 'INSERT INTO todo(name, description, due) VALUES (:name, :description, :due)'
UPDATE_TODO   = 'UPDATE todo SET name=:name, description=:description, due=:due WHERE id=:id'
DELETE_TODO   = 'DELETE FROM todo WHERE id=:id'

def add(todoItem):
    qr = QueryRunner()
    return qr.runDML(INSERT_TODO, **todoItem)

def getAll():
    qr = QueryRunner()
    return qr.runSelect(GET_ALL_TODOS)

def getById(id):
    qr = QueryRunner()
    rows = qr.runSelect(GET_TODO_BYID, id = id)
    return rows[0] if len(rows) > 0 else None

def update(todoItem):
    qr = QueryRunner()
    return qr.runDML(UPDATE_TODO, **todoItem)

def delete(id):
    qr = QueryRunner()
    return qr.runDML(DELETE_TODO, id=id)