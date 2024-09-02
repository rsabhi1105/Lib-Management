# library/tasks.py

from celery import shared_task
from time import sleep

@shared_task
def add(x, y):
    sleep(10)  # Simulate a long-running task
    return x + y
