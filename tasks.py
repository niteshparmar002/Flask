from celery import Celery
from config import *

celery = Celery(__name__)

@celery.task
def add():
    with app.app_context():
        for i in range(1, 100001):
            print(i)
            my_data = User('Nitesh', 'nitesh@segnotech.com', '9351559612')
            db.session.add(my_data)
            db.session.commit()
