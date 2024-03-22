from controller.studentController import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
student = Blueprint('student', __name__)

# @student.route('/')
# def hello_world():
#     return "Hello, World Welcome to the result app! ResultApp"


@student.route("/getAllStudent", methods=['GET'])
def getStudent():
    return get_all_student()


@student.route("/createStudent", methods=['POST'])
def createStudent():
    return create_student()


@student.route("/updateStudent/<matricule>", methods=['PUT'])
def updateStudent(matricule):
    return update_student(matricule)

@student.route("/deleteStudent/<matricule>", methods=['DELETE'])
def deleteStudent(matricule):
    return delete_student(matricule)