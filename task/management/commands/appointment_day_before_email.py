from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone

from task.send_sms import sending_sms


#settings for sending email
from django.core.mail import send_mail
from django.conf import settings

from accounts.models import Appointment, User, Doctor, Assistant, Preference
from datetime import date
import requests
import time
today = date.today()
tomorrow = today + timedelta(1)



class Command(BaseCommand):
    # Sending mail
    
    def handle(self, *args, **options):

        appointments = Appointment.objects.filter(local_appointment_start_date_time__year=tomorrow.year, local_appointment_start_date_time__month=tomorrow.month,local_appointment_start_date_time__day=tomorrow.day)
        if appointments:
            for appointment in appointments:
                print('appointment********************patient', appointment.patient.id)
                print(appointment.patient)
                patient_user_id = appointment.patient.id
                patient_user =  User.objects.get(id=appointment.patient.id)
                patient_email = patient_user.email
                print('patient_email', patient_email)
                patient_phone = patient_user.phone_number
                print('patient_phone', patient_phone)
            
                current_doctor =  Doctor.objects.get(id=appointment.doctor.id)
                # print('doctor',current_doctor.doctor)
                # print('user_id',current_doctor.doctor.id)
                # doctor_user =  User.objects.get(id=current_doctor.doctor.id)
                # doctor_email = doctor_user.email
                # print('doctor_email', doctor_email)


                # current_assistant =  Assistant.objects.get(id=appointment.assistant.id)
                # print('assistant',current_assistant.assistant)
                # print('user_id',current_assistant.assistant.id)
                # assistant_user =  User.objects.get(id=current_assistant.assistant.id)
                # assistant_email = assistant_user.email
                # print('assistant_email', assistant_email)

                appointment_date= appointment.local_appointment_start_date_time
                appointment_date_converted = appointment_date.strftime("%m/%d/%Y %I:%M %p")
                patient_preference = Preference.objects.filter(user_notification=patient_user_id).values()
                print('***********patient_preference**********', patient_preference)
                patient_preference_email_notification = (patient_preference[0]['email_notification'])
                patient_preference_phone_notification = (patient_preference[0]['phone_notification'])
                patient_preference_both_notification = (patient_preference[0]['both_notification'])
                if patient_preference_email_notification == True:
                    print('patient_preference_phone_notification', patient_preference_phone_notification)
                    message = f'You have an appointment with {current_doctor.doctor} at {appointment_date_converted}'
                    subject = 'Appointment Notification'
                    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [patient_email, 'tasmir.project@gmail.com'])
                    self.stdout.write("Day before appointment send")
                if patient_preference_phone_notification == True:
                    # print('***********************************************************patient sms***********************')
                    # url = f"http://66.45.237.70/api.php?username=care71&password=care71@12&number={patient_phone}&message={message}"
                    # payload  = {}
                    # headers = {
                    # 'Content-Type': 'application/x-www-form-urlencoded'
                    # }
                    # response = requests.request("POST", url, headers=headers, data = payload)
                    # # print(response)
                    # # print(response.text.encode('utf8'))
                    sending_sms(patient_phone,message)
                    self.stdout.write("Day before appointment SMS send")
        else:
            self.stdout.write("System has no appointment")

    