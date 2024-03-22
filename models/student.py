# from base_model import AbstractBaseModel
from config.DataSource import DataSource


class Student():
    TABLE_NAME = "student"

    def __init__(self, id=None, name=None, email=None, dob=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.dob = dob
        self.password = password
        self.ds = DataSource()

    def save(self):
        # update student if it exists
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET name=%s ,email=%s ,dob=%s ,password=%s WHERE marticule=%s"
            self.ds.execute(query, (self.name, self.email,
                            self.dob, self.password, self.id))
        else:
            # save into database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (name,email,dob,password) VALUES(%s,%s,%s,%s)"
            self.ds.execute(
                query, (self.name, self.email, self.dob, self.password))
            results = self.ds.execute(
                f"SELECT MAX(marticule) FROM {self.__class__.TABLE_NAME}")
            for result in results:
                new_instance_id = result[0]
            self.id = new_instance_id

    def read(self, id=None):
        if id:
            query = f"SELECT * FROM {self.__class__.TABLE_NAME} WHERE marticule=%s"
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
        print(id)
        if id:
            query = f"DELETE FROM {self.__class__.TABLE_NAME} WHERE marticule=%s"
            self.ds.execute(query, (id,))
            # print(query)
            print("student delete successfully")
        else:
            self.ds.execute(f"DELETE FROM {self.__class__.TABLE_NAME}")
