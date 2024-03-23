from flask import Flask, jsonify, request
from models.student import Student

def get_all_student():
    try:
        return jsonify({"student": Student().read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_student():
    try:
        data = request.get_json()
        student = Student(name=data["name"], email=data["email"],
                          dob=data["dob"], password=data["password"])
        student.save()
        return jsonify({'message': 'Student created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_student(matricule):
    try:
        data = request.get_json()
        student = Student(id=matricule, name=data["name"], email=data["email"],
                          dob=data["dob"], password=data["password"])
        student.save()
        return jsonify({'message': 'Student updated successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_student(matricule):
    try:
        Student().delete(id=matricule)
        return jsonify({'message': 'Student deletes successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
