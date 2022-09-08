from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
#settings for sending email
from django.core.mail import send_mail
from django.conf import settings

from accounts.models import Appointment, User, Doctor, Assistant, Preference
from .tasks import send_email_task, send_sms_task
import requests


#sending sms function
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



@api_view(['GET', 'POST'])
def send_email_celery_view(request):
    if request.method == 'POST':
        message = request.data['message']
        subject = request.data['subject']
        to_email = request.data['to_email']
        # message = 'This is message'
        # subject = 'This is sibject'
        # to_email = 'tasmir.project@gmail.com'
        send_email_task.delay(message,subject,to_email)
        return Response({"message": "Got email data!", "data": request.data})
    return Response({"send_email": "Send email using this api by posint message, subject,to_email field"})



@api_view(['GET', 'POST'])
def send_sms_celery_view(request):
    if request.method == 'POST':
        phone_number = request.data['phone_number']
        message = request.data['message']
        send_sms_task.delay(phone_number,message)
        return Response({"message": "Got sms data!", "data": request.data})
    return Response({"send_sms": "Send sms using this api by possing message, phone_number"})

