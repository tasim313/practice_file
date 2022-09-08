from celery import shared_task
from celery.utils.log import get_task_logger
from django.core.management import call_command # NEW
from time import sleep
import requests
#settings for sending email
from django.core.mail import send_mail
from django.conf import settings
from .send_sms import sending_sms
logger = get_task_logger(__name__)


@shared_task
def sample_task():
    logger.info("The sample task just ran.")

@shared_task
def send_email():
    call_command("send_email", )

@shared_task
def appointment_day_before_email():
    call_command("appointment_day_before_email", )


@shared_task
def doctor_daily_appointment_notification():
    call_command("doctor_daily_appointment_notification", )


@shared_task
def assistant_daily_appointment_notification():
    call_command("assistant_daily_appointment_notification", )


@shared_task
def send_email_task(message,subject,to_email):
    message = message
    subject = subject
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [to_email,])
    print('send email')
    return None



# # sending sms function
# def send_sms(patient_phone,message):
#     send_sms_success = False
#     try:
#         url = f"http://66.45.237.70/api.php?username=care71&password=care71@12&number={patient_phone}&message={message}"
#         payload  = {}
#         headers = {
#         'Content-Type': 'application/x-www-form-urlencoded'
#         }
#         response = requests.request("POST", url, headers=headers, data = payload)
#         send_sms_success = True
#     except:
#         send_sms_success = False
#     return send_sms_success

@shared_task
def send_sms_task(patient_phone,message):
    sending_sms(patient_phone,message)
    print('send sms')
    return None