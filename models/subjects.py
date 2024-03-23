from config.DataSource import DataSource


class Subject():
    TABLE_NAME = "subjects"

    def __init__(self, id=None, title=None, teacher_id=None):
        self.id = id
        self.title = title
        self.teacher_id = teacher_id
        self.ds = DataSource()

    def save(self):
        # update subject if it exists
        if self.id:
            query = f"UPDATE {self.__class__.TABLE_NAME} SET title=%s, teacher_id = %s  WHERE sub_code=%s"
            self.ds.execute(query, (self.title, self.teacher_id, self.id))
        else:
            # save into database
            query = f"INSERT INTO {self.__class__.TABLE_NAME} (title,teacher_id) VALUES(%s,%s)"
            self.ds.execute(query, (self.title, self.teacher_id))
            results = self.ds.execute(
                f"SELECT MAX(sub_code) FROM {self.__class__.TABLE_NAME}")
            for result in results:
                new_instance_id = result[0]
            self.id = new_instance_id

    def read(self, id=None):
        if id:
            query = f"SELECT sub_code,title,name,email FROM {self.__class__.TABLE_NAME} inner join teacher on {self.__class__.TABLE_NAME}.teacher_id=teacher.teacher_id WHERE sub_code=%s"
            # query = f"SELECT (title) FROM {self.__class__.TABLE_NAME} WHERE sub_code=%s"
            result = self.ds.execute(query, (id,))
            return result
        else:
            query = f"SELECT sub_code,title,name,email FROM {self.__class__.TABLE_NAME} inner join teacher on {self.__class__.TABLE_NAME}.teacher_id=teacher.teacher_id"
            results = self.ds.execute(query)
            students = []
            i = 0
            for result in results:
                students.append(result)
            return students

    def delete(self, id=None):
        if id:
            query = f"DELETE FROM {self.__class__.TABLE_NAME} WHERE sub_code=%s"
            self.ds.execute(query, (id,))
            # print(query)
            print("student delete successfully")

        else:
            cursor.execute(f"DELETE FROM {self.__class__.TABLE_NAME}")
