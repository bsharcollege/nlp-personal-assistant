from werkzeug.security import generate_password_hash
from models import db, User
from app import app

with app.app_context():
    db.create_all()
    admin_user = User(
        name='Admin User',
        email='admin_new@example.com',
        role='Admin',
        password=generate_password_hash('adminpassword', method='pbkdf2:sha256')
    )
    db.session.add(admin_user)
    db.session.commit()
    print('Admin user created successfully')