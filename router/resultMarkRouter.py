

from controller.resultMarkController import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
result = Blueprint('result', __name__)


@result.route('/')
def hello_world():
    return "Hello, World Welcome to the result app! ResultApp"


@result.route("/getAllResultMark", methods=['GET'])
def getAllMark():
    return get_all_result()


@result.route("/getStudentResult/<matricule>", methods=['GET'])
def getStudentResult(matricule):
    return get_all_result(id=matricule)


@result.route("/uploadResultMark", methods=['POST'])
def uploadResultMark():
    return uploadedFile()
