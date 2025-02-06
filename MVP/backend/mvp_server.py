# Python server code from earlier

from flask import Flask, jsonify
import logging
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skills.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class PersonalSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

class ProfessionalSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

with app.app_context():
    db.create_all()

@app.route('/api/user')
def get_user():
    app.logger.info('User data requested')
    return jsonify({"me_id": "Me#1", "skills": []})

@app.route('/api/logs')
def get_logs():
    try:
        with open('server.log') as log_file:
            return log_file.read(), 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "No logs found", 404

@app.route('/api/skills/personal')
def get_personal_skills():
    skills = PersonalSkill.query.all()
    return jsonify([skill.name for skill in skills])

@app.route('/api/skills/professional')
def get_professional_skills():
    skills = ProfessionalSkill.query.all()
    return jsonify([skill.name for skill in skills])

if __name__ == '__main__':
    app.run(debug=True)
