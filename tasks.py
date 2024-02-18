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
app = Celery('tasks', backend='redis://:wYn08ptv6hLsvdtKS9MNkrUu@robin.iran.liara.ir:34392/0', broker='redis://:wYn08ptv6hLsvdtKS9MNkrUu@robin.iran.liara.ir:34392/0' ,task_track_started=True,CELERY_TASK_TRACK_STARTED = True )
app.autodiscover_tasks()



@app.task
def add(x,y):
    return x + y


@app.task
def devide(x,y):
    return x / y
