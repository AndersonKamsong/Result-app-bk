

from controller.resultMarkController import *

from flask import Blueprint

# Define your sub-app logic in a separate file (e.g., sub_app.py)
result = Blueprint('result', __name__)

@result.route('/')
def hello_world():
    return "Hello, World Welcome to the result app! ResultApp"

@result.route("/getAllStudent", methods=['GET'])
def resultMark():
    return get_all_result()
    

