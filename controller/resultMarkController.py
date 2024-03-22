import pandas as pd
from flask import Flask, jsonify, request
from models.resultMark import ResultMark
from models.student import Student


def uploadedFile():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    # Get and validate the uploaded file
    uploaded_file = request.files['file']

    if uploaded_file.filename.endswith('.xlsx') or uploaded_file.filename.endswith('.xls'):
        pass  # Valid Excel file
    else:
        return jsonify({'error': 'Invalid file type. Only Excel (.xlsx or .xls) allowed'}), 400

    try:
        # Read the Excel data into a DataFrame
        df = pd.read_excel(uploaded_file)
        # Convert DataFrame to a list of dictionaries (JSON format)
        data = df.to_dict(orient='records')
        print(data)
        # Call function to store data in MySQL

        return jsonify({'message': 'Data uploaded and stored successfully!'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500


def get_all_result():
    try:
        return jsonify({"result": ResultMark().read()}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def update_result():
    try:
        CAmarks = request.form.get('CAmarks')
        Examsmarks = request.form.get('Examsmarks')
        Resistmarks = request.form.get('Resistmarks')
        marticule = request.form.get('marticule')
        sub_code = request.form.get('sub_code')
        student = ResultMark(CAmarks, Examsmarks,
                             Resistmarks, marticule, sub_code)
        student.updateMark(marticule, sub_code)
        return jsonify({'message': 'Result update successfully!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
