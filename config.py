from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

app = Flask(__name__)
app.secret_key = "Secret Key"

# Redis configuration (additional)
app.config['CELERY_REDIS_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_REDIS_RESULT_BACKEND'] = 'redis://localhost:6379/0'

# Create Celery instance for Redis
celery_redis = Celery(
    app.import_name,
    backend=app.config['CELERY_REDIS_RESULT_BACKEND'],
    broker=app.config['CELERY_REDIS_BROKER_URL']
)
celery_redis.conf.update(app.config)

# Update the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://flask:flask@localhost/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(100))

    def __repr__(self):
        return f"User('{self.name}')"
    
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

# Create the database and tables
with app.app_context():
    db.create_all()