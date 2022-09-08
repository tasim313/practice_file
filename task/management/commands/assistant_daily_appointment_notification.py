from datetime import timedelta, time, datetime

from django.core.mail import mail_admins
from django.core.management import BaseCommand
from django.utils import timezone
from django.utils.timezone import make_aware
from task.send_sms import sending_sms
#settings for sending email
from django.core.mail import send_mail
from django.conf import settings
import requests
from accounts.models import Appointment, User, Doctor, Assistant, Preference
from datetime import date
import time

today = date.today()
tomorrow = today + timedelta(1)
print()


class Command(BaseCommand):
    # Sending mail to dactor for daily appointment
    
    def handle(self, *args, **options):
        all_assistant_user_id = User.objects.all().filter(is_assistant=True).values_list('id', flat=True)
        for assistant_user_id in all_assistant_user_id:
            assistant_profile_id = Assistant.objects.filter(assistant__id=assistant_user_id).values()
            assistant_user_info = User.objects.get(id=assistant_user_id)
            assistant_email = assistant_user_info.email            
            assistant_phone = assistant_user_info.phone_number
            print('assistant_phone', assistant_phone)            
            #email, text, both notification preferences
            assistant_preference = Preference.objects.filter(user_notification=assistant_user_id).values()
            assistant_preference_email_notification = (assistant_preference[0]['email_notification'])
            assistant_preference_phone_notification = (assistant_preference[0]['phone_notification'])
            assistant_preference_both_notification = (assistant_preference[0]['both_notification'])
            try:
                appointments = Appointment.objects.filter(local_appointment_start_date_time__year=tomorrow.year, local_appointment_start_date_time__month=tomorrow.month,local_appointment_start_date_time__day=tomorrow.day, assistant_id=assistant_profile_id[0]['id']).values()
                if appointments:
                    if assistant_preference_email_notification == True:
                        print(appointments)
                        print(len(appointments))
                        print(assistant_email)
                        print('assistant_preference_phone_notification', assistant_preference_phone_notification)
                        
                        message = f'Hello, {assistant_user_info} .You have {len(appointments)} appointment on {tomorrow}'
                        subject = 'Assistant Appointment Notification'
                        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [assistant_email, 'tasmir.project@gmail.com'])
                        self.stdout.write("Assistant daily appointment notification send")
                    if assistant_preference_phone_notification == True:
                        # print('***********************************************************doctor sms***********************')
                        # assis_sms_url = f"http://66.45.237.70/api.php?username=care71&password=care71@12&number={assistant_phone}&message={message}"
                        # payload  = {}
                        # headers = {
                        # 'Content-Type': 'application/x-www-form-urlencoded'
                        # }
                        # response = requests.request("POST", assis_sms_url, headers=headers, data = payload)
                        # # print(response)
                        # # print(response.text.encode('utf8'))
                        sending_sms(assistant_phone,message)
                        self.stdout.write("Day before appointment Assistant SMS send")
            except:
                self.stdout.write("Assistant have no appointment tomorrow")

    