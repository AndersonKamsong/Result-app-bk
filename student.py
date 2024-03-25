import mysql.connector
from base_model import AbstractBaseModel

class Student(AbstractBaseModel):
    TABLE_NAME = "Student"

    def __init__(self, matricule=None, name=None, email=None, password=None):
        self.matricule = matricule
        self.name = name
        self.email = email
        self.password = password

    def save(self):
        if self.matricule:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET name=%s, email=%s, password=%s WHERE matricule=%s"
            values = (self.name, self.email, self.password, self.matricule)
        else:
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (name, email, password) VALUES(%s, %s, %s)"
            values = (self.name, self.email, self.password)

        with mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="database_name"
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(query, values)

            if not self.matricule:
                new_instance_matricule = cursor.lastrowid
                self.matricule = new_instance_matricule

    @classmethod
    def read(cls, matricule=None):
        with mysql.connector.connect(
            host="localhost",
            user="username",
            password="password",
            database="database_name"
        ) as connection:
            cursor = connection.cursor()
            if matricule:
                query = f"SELECT matricule, name, email, password FROM {cls.TABLE_NAME} WHERE matricule=%s"
                values = (matricule, )
                cursor.execute(query, values)

                result = cursor.fetchone()
                if result:
                    student = cls(matricule=result[0], name=result[1], email=result[2], password=result[3])
                    return student
            else:
                query = f"SELECT matricule, name, email, password FROM {cls.TABLE_NAME}"
                cursor.execute(query)

                results = cursor.fetchall()
                stdent = []

                for result in results:
                    student = cls(matricule=result[0], name=result[1], email=result[2], password=result[3])
                    student.append(student)

                return stdent

    def update(self):
        if self.matricule:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET name=%s, email=%s, password=%s WHERE matricule=%s"
            values = (self.name, self.email, self.password, self.matricule)

            with mysql.connector.connect(
                host="localhost",
                user="username",
                password="password",
                database="database_name"
            ) as connection:
                cursor = connection.cursor()
                cursor.execute(query, values)