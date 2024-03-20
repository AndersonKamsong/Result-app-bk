import pandas as pd
from flask import Flask, jsonify, request

def uploadedFile():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    # Get and validate the uploaded file
    uploaded_file = request.files['file']
    # print(uploaded_file)
    if uploaded_file.filename.endswith('.xlsx') or uploaded_file.filename.endswith('.xls'):
        # print("passing")
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
