import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BamniApi.settings")

app = Celery("BamniApi")

#timezone settings
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Dhaka')

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()