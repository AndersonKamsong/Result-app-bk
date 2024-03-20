from flask import Flask, request, render_template
from subject_model import Subject

app = Flask(__name__)

@app.route("/")
def index():
    subjects = Subject.read()
    return render_template("index.html", subjects=subjects)

@app.route("/subject/<int:subject_id>")
def get_subject(subject_id):
    subject = Subject.read(subject_id)
    if subject:
        return render_template("subject.html", subject=subject)
    else:
        return "Subject not found", 404

@app.route("/subject", methods=["POST"])
def create_subject():
    name = request.form["name"]
    duration = int(request.form["duration"])  # Assuming duration is provided as an integer
    subject = Subject(name=name, duration=duration)
    subject.create()
    return "Subject created successfully", 201

@app.route("/subject/<int:subject_id>", methods=["PUT"])
def update_subject(subject_id):
    name = request.form["name"]
    duration = int(request.form["duration"])  # Assuming duration is provided as an integer
    subject = Subject.read(subject_id)
    if subject:
        subject.name = name
        subject.duration = duration
        subject.update()
        return "Subject updated successfully", 200
    else:
        return "Subject not found", 404

@app.route("/subject/<int:subject_id>", methods=["DELETE"])
def delete_subject(subject_id):
    subject = Subject.read(subject_id)
    if subject:
        subject.delete()
        return "Subject deleted successfully", 200
    else:
        return "Subject not found", 404

if __name__ == "__main__":
    app.run(debug=True)
