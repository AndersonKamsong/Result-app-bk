# from base_model import AbstractBaseModel
from config.DataSource import DataSource


class ResultMark():
    TABLE_NAME = "resultsMark"

    def __init__(self, id=None, name=None, email=None, dob=None, password=None):
        self.marticule = marticule
        self.sub_code = sub_code
        self.CAmarks = CAmarks
        self.Examsmarks = Examsmarks
        self.Resistmarks = Resistmarks
        self.ds = DataSource()

    def updateMark(self,marticule,sub_code):
        # update student if it exists
        query = f"UPDATE {self.__class__.TABLE_NAME} SET CAmarks=%s,Examsmarks=%s,Resistmarks=%s WHERE  marticule=%s, sub_code=%s"
        self.ds.execute(query, (self.CAmarks,self.Examsmarks,self.Resistmarks,marticule,sub_code,))

    def save(self):
        # save into database
        query = f"INSERT INTO {self.__class__.TABLE_NAME} (CAmarks,Examsmarks,Resistmarks,marticule,sub_code) VALUES(%s,%s,%s,%s,%s)"
        self.ds.execute(query, (self.CAmarks,self.Examsmarks,self.Resistmarks,self.marticule,self.sub_code,))
        

    def read(self, id=None):
        if id:
            # SELECT * FROM student inner join resultsMark on student.marticule=resultsMark.marticule inner join subjects on resultsMark.sub_code = subjects.sub_code;
            query = f"SELECT * FROM student inner join resultsMark on student.marticule=resultsMark.marticule inner join subjects on resultsMark.sub_code = subjects.sub_code WHERE marticule=%s"
            result = self.ds.execute(query, (id,))
            return result
        else:
            query = f"SELECT * FROM student inner join resultsMark on student.marticule=resultsMark.marticule inner join subjects on resultsMark.sub_code = subjects.sub_code"
            results = self.ds.execute(query)
            students = []
            for result in results:
                students.append(result)
            return students

