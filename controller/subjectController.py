from flask import Flask, jsonify, request
from models.subjects import Subject


def get_all_subject():
    try:
        return jsonify({"subjects": Subject().read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def create_subject():
    try:
        data = request.get_json()
        subject = Subject(title=data["title"], teacher_id=data["teacher_id"])
        subject.save()
        return jsonify({'message': 'subject created successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_subject(sub_code):
    try:
        data = request.get_json()
        subject = Subject(id=sub_code, title=data["title"],
                          teacher_id=data["teacher_id"])
        subject.save()
        return jsonify({'message': 'subject updated successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def delete_subject(sub_code):
    try:
        Subject().delete(id=sub_code)
        return jsonify({'message': 'subject deleted successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
