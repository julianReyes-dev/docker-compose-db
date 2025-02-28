from flask import Flask, request, jsonify
from models import db, Student

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/students_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{'id': s.id, 'nombre': s.nombre, 'edad': s.edad, 'carrera': s.carrera} for s in students])

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    new_student = Student(nombre=data['nombre'], edad=data['edad'], carrera=data['carrera'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({'id': new_student.id, 'nombre': new_student.nombre, 'edad': new_student.edad, 'carrera': new_student.carrera}), 201

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({'id': student.id, 'nombre': student.nombre, 'edad': student.edad, 'carrera': student.carrera})

@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.nombre = data['nombre']
    student.edad = data['edad']
    student.carrera = data['carrera']
    db.session.commit()
    return jsonify({'id': student.id, 'nombre': student.nombre, 'edad': student.edad, 'carrera': student.carrera})

@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
