from controller.subjectController import *
from flask import Blueprint

subject = Blueprint('subject', __name__)

@subject.route("/")
def index():
    subjects = Subject.read() 
    # Convert subject data to a JSON format 
    subjects_data = [{"id": subject.id, "name": subject.name, "duration": subject.duration} for subject in subjects]
    return jsonify(subjects_data)

@subject.route("/subject/<int:subject_id>")
def get_subject(subject_id):
    subject = Subject.read(subject_id)
    if subject:
        # Convert subject data to a JSON format
        subject_data = {"id": subject.id, "name": subject.name, "duration": subject.duration}
        return jsonify(subject_data)
    else:
        return jsonify({"error": "Subject not found"}), 404

@subject.route("/subject", methods=["POST"])
def create_subject():
    name = request.form["name"]
    duration = int(request.form["duration"])  # Assuming duration is provided as an integer
    subject = Subject(name=name, duration=duration)
    subject.create()
    return "Subject created successfully", 201

@subject.route("/subject/<int:subject_id>", methods=["PUT"])
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

@subject.route("/subject/<int:subject_id>", methods=["DELETE"])
def delete_subject(subject_id):
    subject = Subject.read(subject_id)
    if subject:
        subject.delete()
        return "Subject deleted successfully", 200
    else:
        return "Subject not found", 404