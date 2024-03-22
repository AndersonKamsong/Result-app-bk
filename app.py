
from flask import Flask
from router.resultMarkRouter import result
from router.studentRouter import student

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World Welcome to the result app!"

# Optional URL prefix
app.register_blueprint(result, url_prefix='/api/result')
app.register_blueprint(student, url_prefix='/api/student')


if __name__ == "__main__":
    app.run(debug=True)
