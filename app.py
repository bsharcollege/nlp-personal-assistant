# filepath: /C:/Users/bhask/code/nlp_project/nlp-personal-assistant/src/app.py
from flask import Flask, request, jsonify, render_template, redirect, url_for, session, flash
from flask_migrate import Migrate
from models import db, User
from calendar_management import CalendarManager
from main import NLPPersonalAssistant
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nlp_personal_assistant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

migrate = Migrate(app, db)

calendar_manager = CalendarManager()
assistant = NLPPersonalAssistant()

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.user_id
            session['role'] = user.role
            return redirect(url_for('index'))
        flash('Invalid email or password')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('role', None)
    return redirect(url_for('login'))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('message')
    response = assistant.process_input(user_input)
    return jsonify({'response': response})

@app.route('/create_reminder', methods=['POST'])
def create_reminder():
    data = request.json
    subject = data.get('subject')
    start_time = data.get('start_time', datetime.now().isoformat())
    reminder = calendar_manager.create_reminder(subject, start_time)
    return jsonify(reminder)

@app.route('/get_reminders', methods=['GET'])
def get_reminders():
    reminders = calendar_manager.get_reminders()
    return jsonify(reminders)

@app.route('/users', methods=['POST'])
def add_user():
    if 'role' not in session or session['role'] != 'Admin':
        return jsonify({'message': 'Access denied'}), 403

    data = request.json
    name = data.get('name')
    email = data.get('email')
    role = data.get('role', 'User')
    password = generate_password_hash(data.get('password'), method='pbkdf2:sha256')
    new_user = User(name=name, email=email, role=role, password=password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users', methods=['GET'])
def get_users():
    if 'role' not in session or session['role'] != 'Admin':
        return jsonify({'message': 'Access denied'}), 403

    users = User.query.all()
    users_list = [{'user_id': user.user_id, 'name': user.name, 'email': user.email, 'role': user.role} for user in users]
    return jsonify(users_list)

@app.route('/manage_users', methods=['GET'])
def manage_users():
    if 'role' not in session or session['role'] != 'Admin':
        return jsonify({'message': 'Access denied'}), 403

    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)