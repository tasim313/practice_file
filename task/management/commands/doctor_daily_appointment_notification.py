from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from task.send_sms import sending_sms
#settings for sending email
from django.core.mail import send_mail
from django.conf import settings
from accounts.models import Appointment, User, Doctor, Assistant, Preference
from datetime import date
today = date.today()
tomorrow = today + timedelta(1)
import time

# print("Printed immediately.")
# time.sleep(2.4)
# print("Printed after 2.4 seconds.")



class Command(BaseCommand):
    # Sending mail to dactor for daily appointment
    
    def handle(self, *args, **options):
        all_doctor_user_id = User.objects.all().filter(is_doctor=True).values_list('id', flat=True)
        for doctor_user_id in all_doctor_user_id:
            doctor_profile_id = Doctor.objects.filter(doctor__id=doctor_user_id).values()
            doctor_user_info = User.objects.get(id=doctor_user_id)
            doctor_email = doctor_user_info.email
            doctor_phone = doctor_user_info.phone_number
            print('doctor_phone', doctor_phone)
            #email, text, both notification preferences
            doctor_preference = Preference.objects.filter(user_notification=doctor_user_id).values()
            doctor_preference_email_notification = (doctor_preference[0]['email_notification'])
            doctor_preference_phone_notification = (doctor_preference[0]['phone_notification'])
            doctor_preference_both_notification = (doctor_preference[0]['both_notification'])
            try:
                appointments = Appointment.objects.filter(local_appointment_start_date_time__year=tomorrow.year, local_appointment_start_date_time__month=tomorrow.month,local_appointment_start_date_time__day=tomorrow.day, doctor_id=doctor_profile_id[0]['id']).values()
                if appointments:
                    if doctor_preference_email_notification == True:
                        print(appointments)
                        print(len(appointments))
                        print(doctor_email)
                        print('doctor_preference_phone_notification', doctor_preference_phone_notification)
                        
                        message = f'Hello, {doctor_user_info} .You have {len(appointments)} appointment on {tomorrow}'
                        subject = 'Doctor Appointment Notification'
                        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [doctor_email, 'tasmir.project@gmail.com'])
                        self.stdout.write("Doctor daily appointment notification send")
                    if doctor_preference_phone_notification == True:
                        # print('***********************************************************doctor sms***********************')
                        # doc_sms_url = f"http://66.45.237.70/api.php?username=care71&password=care71@12&number={doctor_phone}&message={message}"
                        # payload  = {}
                        # headers = {
                        # 'Content-Type': 'application/x-www-form-urlencoded'
                        # }
                        # response = requests.request("POST", doc_sms_url, headers=headers, data = payload)
                        # # print(response)
                        # # print(response.text.encode('utf8'))
                        sending_sms(doctor_phone,message)
                        self.stdout.write("Day before appointment Doctor SMS send")
            except:
                self.stdout.write("Doctor have no appointment tomorrow")

    