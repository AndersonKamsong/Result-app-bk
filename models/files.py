import sqlite3
from base_model import AbstractBaseModel

class Files(AbstractBaseModel):
    TABLE_NAME="Files"

    def __init__(self,id=None,path=None):
        self.id = id
        self.path = path

    def save(self):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()
        #if file already exists, update the path
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET path=? WHERE id=?"
            cursor.execute(query,(self.path,self.id))
        
        #save into database otherwise
        else:
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (path) VALUES(?)"
            cursor.execute(query,self.path)
            
            new_instance_id = cursor.execute(f"SELECT MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone[0]

            self.id = new_instance_id
    
    def read(self,id=None):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()
        
        #read file with given id
        if id:
            query = f"SELECT (path) FROM {self.__class__.TABLE_NAME} WHERE id=?"
            result = cursor.execute(query,id).fetchone()
            file = Files(path=result[1])
            file.id = result[0]

            return file
        
        #otherwise read all
        else:
            query = f"SELECT (path) FROM {self.__class__.TABLE_NAME}"
            results = cursor.execute(query).fetchall()

            files = []

            for result in results:
                file = Files(path=result[1])
                file.id = result[0]

                files.append[file]

                return files
    
    def delete(self):
        with sqlite3.connect("db.sqlite") as connection:
            cursor = connection.cursor()

        #delete by id
        if self.id:
            cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?",(self.id))
        
        #otherwise delete all
        else:
            cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME}")
        

        

