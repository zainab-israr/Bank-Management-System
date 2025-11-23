import sqlite3

class Database:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
    
    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            balance REAL NOT NULL
        )
        ''')
        self.conn.commit()
    
    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
    
    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()
    
    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()
