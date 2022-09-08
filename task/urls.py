from django.urls import include, path

from .views import *

urlpatterns = [
    path("send_email", send_email_celery_view),
    path("send_sms", send_sms_celery_view),
]
