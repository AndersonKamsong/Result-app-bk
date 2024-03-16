import sqlite3
from base_model import AbstractBaseModel

class Subjects(AbstractBaseModel):
    TABLE_NAME = "Subjects"

    def __init__(self,id=None,name=None):
        self.id = id
        self.name = name
    
    def save(self):
        # update subject if it exists
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET name=? WHERE id=?"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query,(self.name,self.id))
        else:
            #save into database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (name) VALUES(?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query,(self.name))

                new_instance_id = cursor.execute(f"SELECT * MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id = new_instance_id
    
    def read(self,id=None):
        with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor() 
        if id:
            query = f"SELECT (name) FROM {self.__class__.TABLE_NAME} WHERE id=?"
            result = cursor.execute(query,id).fetchone()
            subject = Subjects(name=result[1])
            subject.id = result[0]

            return subject
        else:
            query = f"SELECT (name) FROM {self.__class__.TABLE_NAME}"
            results = cursor.execute(query).fetchall()

            subjects = []

            for result in results:
                subject = Subjects(name=result[1])
                subject.id = result[0]


                subjects.append[subject]

                return subjects
    
    def delete(self):
        with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
        #delete by id
        if self.id:
            cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?",(self.id))

        else:
             cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME}")

                