# from base_model import AbstractBaseModel
from config.DataSource import DataSource


class Teacher():
    TABLE_NAME = "teacher"

    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.ds = DataSource()

    def save(self):
        # update student if it exists
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET name=%s ,email=%s ,password=%s WHERE teacher_id=%s"
            self.ds.execute(
                query, (self.name, self.email, self.password, self.id))
        else:
            # save into database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (name,email,password) VALUES(%s,%s,%s)"
            self.ds.execute(query, (self.name, self.email, self.password))
            results = self.ds.execute(
                f"SELECT MAX(teacher_id) FROM {self.__class__.TABLE_NAME}")
            for result in results:
                new_instance_id = result[0]
            self.id = new_instance_id

    def read(self, id=None):
        if id:
            query = f"SELECT * FROM {self.__class__.TABLE_NAME} WHERE teacher_id=%s"
            result = self.ds.execute(query, (id,))
            return result
        else:
            query = f"SELECT * FROM {self.__class__.TABLE_NAME}"
            results = self.ds.execute(query)
            students = []
            i = 0
            for result in results:
                students.append(result)
            return students

    def delete(self, id=None):
        # delete by id
        if id:
            query = f"DELETE FROM {self.__class__.TABLE_NAME} WHERE teacher_id=%s"
            self.ds.execute(query, (id,))
            # print("teacher delete successfully")
        else:
            self.ds.execute(f"DELETE FROM {self.__class__.TABLE_NAME}")
