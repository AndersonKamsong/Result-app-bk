from controller.teacherController import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
teacher = Blueprint('teacher', __name__)



@teacher.route("/getAllTeacher", methods=['GET'])
def getTeacher():
    return get_all_teacher()


@teacher.route("/createTeacher", methods=['POST'])
def createTeacher():
    return create_teacher()


@teacher.route("/updateTeacher/<teacher_id>", methods=['PUT'])
def updateTeacher(teacher_id):
    return update_teacher(teacher_id)

@teacher.route("/deleteTeacher/<teacher_id>", methods=['DELETE'])
def deleteTeacher(teacher_id):
    return delete_teacher(teacher_id)