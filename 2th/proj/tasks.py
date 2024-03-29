from __future__ import absolute_import, unicode_literals
from .celery import app


@app.task
def add(x, y):
    return x+y


@app.task(ignore_result=True)
def devide(x, y):
    return x / y


@app.task
def average(l):
    return sum(l) / len(l)