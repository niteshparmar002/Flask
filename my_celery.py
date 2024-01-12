from celery import Celery
from flask import Flask

def make_celery(app: Flask):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_REDIS_RESULT_BACKEND'],
        broker=app.config['CELERY_REDIS_BROKER_URL']
    )
    celery.conf.update(app.config)
    return celery
