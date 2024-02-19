from celery import Celery
import logging

# BROKER_URL = 'redis://127.0.0.1:6379'
# CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'
# CELERY_BROKER_URL ='redis://127.0.0.1:6379'
# broker_connection_retry_on_startup=True
# app = Celery('tasks', broker='redis://localhost')
CELERY_TASK_TRACK_STARTED = True
task_track_started = True
broker_connection_retry_on_startup = True
app = Celery('tasks', broker='redis://localhost:6379' ,task_track_started=True,CELERY_TASK_TRACK_STARTED = True )

# app.conf.result_backend ='redis://localhost:6379/'
# app.conf.update(
#     task_serializer='json',
#     accept_content=['json'],  # Ignore other content
#     result_serializer='json',
#     timezone='Asia/tehran',
#     enable_utc=True,
# )
app.config_from_object('celeryconfig')

@app.task
def add(x,y):
    return x + y


@app.task
def devide(x,y):
    return x / y
