from controller.subjectController import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
subject = Blueprint('subject', __name__)



@subject.route("/getAllSubject", methods=['GET'])
def getSubject():
    return get_all_subject()


@subject.route("/createSubject", methods=['POST'])
def createSubject():
    return create_subject()


@subject.route("/updateSubject/<sub_code>", methods=['PUT'])
def updateSubject(sub_code):
    return update_subject(sub_code)

@subject.route("/deleteSubject/<sub_code>", methods=['DELETE'])
def deleteSubject(sub_code):
    return delete_subject(sub_code)