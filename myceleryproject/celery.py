import os
from celery import Celery
from time import sleep

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myceleryproject.settings')

app= Celery('myceleryproject')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# addititng tasks

@app.task
def add(x,y):
      sleep(10)
      return x + y

# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')