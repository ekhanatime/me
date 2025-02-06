# Python server code from earlier

from flask import Flask, jsonify, request
import logging
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user
from werkzeug.security import generate_password_hash, check_password_hash

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

login_manager = LoginManager()
login_manager.init_app(app)

class PersonalSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

class ProfessionalSkill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(128))
    google_id = db.Column(db.String(21))
    facebook_id = db.Column(db.String(21))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'status': 'success'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        login_user(user)
        return jsonify({'status': 'success', 'user_id': user.id})
    return jsonify({'status': 'invalid credentials'}), 401

if __name__ == '__main__':
    app.run(debug=True)
