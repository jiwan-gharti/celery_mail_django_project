import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mainapp.settings')

app = Celery('mainapp')
app.config_from_object("django.conf:settings",'CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
}



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')