# Flask API (Flask + SQLAlchemy + MySQL)
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@localhost/{os.getenv('DB_NAME')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)


with app.app_context():
    db.create_all()


@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in tasks])


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    return jsonify({'id': task.id, 'title': task.title, 'completed': task.completed})


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = Task(title=data['title'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task created'}), 201


@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.json
    task = Task.query.get(id)
    task.title = data['title']
    task.completed = data['completed']
    db.session.commit()
    return jsonify({'message': 'Task updated'})


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'})


if __name__ == '__main__':
    app.run(debug=True)
