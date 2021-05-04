from flask import g

class QueryRunner():
    def __init__(self, conn = None):        
        self.connection = conn if conn else g.connection
    
    def runDDL(self, ddl):
        self.connection.executescript(ddl)
        self.connection.commit()        
    
    def runSelect(self, sql, **params):
        cursor = self.connection.cursor()
        rows = cursor.execute(sql, params).fetchall()
        cursor.close()
        return rows
    
    def runDML(self, dml, **params):
        cursor = self.connection.cursor()
        affectedRowData= cursor.execute(dml, params)
        cursor.close()
        self.connection.commit()
        return affectedRowData
