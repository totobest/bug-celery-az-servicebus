# Create your tasks here

from celery import shared_task


@shared_task(ignore_result=True)
def add(x, y):
    return x + y
