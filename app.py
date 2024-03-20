
from config.DataSource import DataSource
from models.resultMark import ResultMark
from models.student import Student

ds = DataSource()
# cursor = ds.create_cursor()
name = "Anderson2"
email = "kamsonganderson3@gmail.com"
dob = "2024-05-11"
password = "Anderson"

# ds.execute("INSERT INTO student (name,email,dob,password) VALUES (%s,%s,%s,%s)",
#             (name,email,dob,password))
# results = ds.execute("SELECT * FROM student")
# for row in results:
#     print(row)
student = Student(id=7,name = "good12",email = "kamsonganderson3@gmail.com",dob = "2024-05-11",password = "Anderson")
student.delete()
print(ResultMark().read())