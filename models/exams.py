import sqlite3
from base_model import AbstractBaseModel
class Exams(AbstractBaseModel):
    TABLE_NAME = "Exams"

    def __init__(self,id=None,subject=None,academic_year=None,
                 session=None,duration=None):
        self.id = id
        self.subject = subject
        self.academic_year = academic_year
        self.session = session
        self.duration = duration

    def save(self):
        # if id exists already, update the exam
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET subject=?,academic_year=?,
            session=?, duration=? WHERE id=?"

            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query, (self.subject,self.academic_year,self.session,self.duration,self.id))
        
        #save into database otherwise
        else:
            query = f"INSERT INTO {self.__class__.TABLE_NAME}(subject,academic_year,session,duration) VALUES(?,?,?,?)"
            with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                cursor.execute(query,(self.subject,self.academic_year,self.session,self.duration))

                new_instance_id = cursor.execute(f"SELECT * MAX(id) FROM {self.__class__.TABLE_NAME}").fetchone()[0]

                self.id = new_instance_id

    def read(self,id=None):
        with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()
                
        if id:
            query = f"SELECT (id,subject,academic_year,session,duration) FROM {self.__class__.TABLE_NAME} WHERE id=?"
            result = cursor.execute(query,id).fetchone()
            exam = Exams(subject=result[1],academic_year=result[2],session=result[3],duration=result[4])
            exam.id = result[0]

            return exam

            
        else:
            query = f"SELECT (id,subject,academic_year,session,duration) FROM {self.__class__.TABLE_NAME}"
            results = cursor.execute(query).fetchall()

            exams = []

            for result in results:
                exam == Exams(subject=result[1],academic_year=result[2],session=result[3],duration=result[4])

                exam.id = result[0]

                exams.append(exam)
                
                return exams
            
    def delete(self):
        with sqlite3.connect("db.sqlite") as connection:
                cursor = connection.cursor()

        if self.id:
            cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME} WHERE id=?",(self.id))
        
        else:
             cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME}")

        
        