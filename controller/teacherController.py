from flask import Flask, jsonify, request
from models.teacher import Teacher


def get_all_teacher():
    try:
        return jsonify({"teachers": Teacher().read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_teacher():
    try:
        data = request.get_json()
        teacher = Teacher(name=data["name"], email=data["email"],
                          password=data["password"])
        teacher.save()
        return jsonify({'message': 'teacher created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_teacher(teacher_id):
    try:
        data = request.get_json()
        teacher = Teacher(id=teacher_id, name=data["name"], email=data["email"],
                          password=data["password"])
        teacher.save()
        return jsonify({'message': 'Teacher updated successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_teacher(teacher_id):
    try:
        Teacher().delete(id=teacher_id)
        return jsonify({'message': 'Teacher deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
