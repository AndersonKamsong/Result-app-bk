
from flask import Flask
from router.resultMarkRouter import result
from router.studentRouter import student
from router.teacherRouter import teacher
from router.subjectRouter import subject

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World Welcome to the result app!"

# Optional URL prefix
app.register_blueprint(result, url_prefix='/api/result')
app.register_blueprint(student, url_prefix='/api/student')
app.register_blueprint(teacher, url_prefix='/api/teacher')
app.register_blueprint(subject, url_prefix='/api/subject')


if __name__ == "__main__":
    app.run(debug=True)
