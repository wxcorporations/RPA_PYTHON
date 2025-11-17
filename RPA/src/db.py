import sqlite3
from datetime import datetime


class DataBase:
    def __init__(self):
        self.connect = sqlite3.connect('reports.db')
        self.cursor = self.connect.cursor()
        
        self.__create_table_file_category()
        self.__create_table_reports()
        self.__create_table_uploads()


    # table upload 
    # -------------------------------------------------------------
    def __create_table_uploads(self):
        command = '''
            CREATE TABLE IF NOT EXISTS uploads (
                name TEXT PRIMARY KEY,
                create_at DATETIME,
                is_process BOOLEAN,
                woner VARCHAR(100)
            );
        '''
        self.cursor.execute(command)
        self.connect.commit()

    def save_file(self, name, woner, is_process=0):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        command = '''
            INSERT INTO uploads (name, create_at, is_process, woner)
            VALUES (?,?,?,?)
        '''
        self.cursor.execute(command, (name, agora, is_process, woner))
        self.connect.commit()
        
    def update_file_id(self, hash):
        command = '''
            UPDATE uploads SET is_process = ?
            WHERE name = ?
        '''
        data = (1, hash)
        self.cursor.execute(command, data)
        self.connect.commit()

    def get_pendings(self):
        command = '''
            SELECT * FROM uploads
            WHERE is_process = 0
            ORDER BY create_at LIMIT 1
        '''
        return self.cursor.execute(command).fetchall()


    # table reports 
    # -------------------------------------------------------------
    def __create_table_reports(self):
        command = '''
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                crate_at DATETIME,
                itens NUMBER,
                size NUMBER,
                category INTEGER,
                FOREIGN KEY (category) REFERENCES file_category(id)
            );
        '''
        self.cursor.execute(command)
        self.connect.commit()
    
    def save_report(self, name, itens, size, category):
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        command = '''
            INSERT INTO reports (crate_at, name, itens, size, category)
            VALUES (?,?,?,?,?)
        '''
        self.cursor.execute(command, (agora, name, itens, size, category))
        self.connect.commit()
    
        
    # table file category
    # -------------------------------------------------------------
    def __create_table_file_category(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_category (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            );
        ''')
        
        self.connect.commit()

    def save_category(self, name):
        self.cursor.execute('''
            INSET INTO file_category (name)
            VALUES (?)
        ''', (name))
        self.connect.commit()

    def rollback(self):
        self.connect.rollback()
