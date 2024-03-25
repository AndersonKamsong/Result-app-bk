from flask import Flask, request, jsonify

app = Flask(__name__)

class Student:
    TABLE_NAME = "Students"

    # Rest of the Student class implementation...

# Routes and controller functions...

if __name__ == '__main__':
    app.run()

app = Flask(__name__)

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    student = Student(matricule=data['matricule'], name=data['name'], email=data['email'], password=data['password'])
    student.save()
    return jsonify({'message': 'Student created successfully'})

@app.route('/students/<matricule>', methods=['GET'])
def get_student(matricule):
    student = Student.read(matricule=matricule)
    if student:
        return jsonify({'matricule': student.matricule, 'name': student.name, 'email': student.email, 'password': student.password})
    else:
        return jsonify({'message': 'Student not found'})

@app.route('/students/<matricule>', methods=['PUT'])
def update_student(matricule):
    data = request.get_json()
    student = Student.read(matricule=matricule)
    if student:
        student.name = data['name']
        student.email = data['email']
        student.password = data['password']
        student.update()
        return jsonify({'message': 'Student updated successfully'})
    else:
        return jsonify({'message': 'Student not found'})

if __name__ == '__main__':
    app.run()