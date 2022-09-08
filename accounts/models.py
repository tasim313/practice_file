from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db.models.signals import post_save
from PIL import Image


# def nameFile(instance, filename):
#     return '/'.join(['images', str(instance.doctor.username), filename])

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, phone_number, is_patient, is_doctor, is_laboratory,
                    is_pharmacy, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, username,
        first name, last name, phone number and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have an username')
        if not first_name:
            raise ValueError('Users must have to give there first name')
        if not last_name:
            raise ValueError('Users must have to give there last name')
        if not phone_number:
            raise ValueError('User must have to give there phone number')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            is_patient=is_patient,
            is_doctor=is_doctor,
            is_laboratory=is_laboratory,
            is_pharmacy=is_pharmacy,
            # is_assistant=is_assistant,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a Staff User with the given email, username,
        first name, last name, phone number and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, first_name, last_name, password, **extra_fields):
        """
        Creates and saves a Super User with the given email, username,
        first name, last name, phone number and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            **extra_fields,
        )

        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        verbose_name='username',
        max_length=255,
        unique=True,
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    nid_number = models.CharField(max_length=255, blank=True, null=True)

    # bhamni
    identifier = models.CharField(max_length=255, blank=True, null=True)
    bhamniuuid = models.CharField(max_length=255, blank=True, null=True)
    create_account = models.BooleanField(default=False)
    account_created = models.BooleanField(default=False)

    profile_picture = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        blank=True,
        null=True,
    )
    joining_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # User Type
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_laboratory = models.BooleanField(default=False)
    is_pharmacy = models.BooleanField(default=False)
    is_assistant = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone_number', 'is_patient', 'is_doctor',
                       'is_laboratory', 'is_pharmacy', 'is_assistant']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    # def save(self, *args, **kwargs):
    #     user = super(User, self).save(self, *args, **kwargs)
    #     if self.is_patient:
    #         group = Group.objects.get(name='Passient')
    #         user.groups.add(group)
    #         user.save()


class Doctor(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user_doctor')
    degree = models.CharField(max_length=255, blank=True, null=True)
    specialist = models.CharField(max_length=255, blank=True, null=True)
    # office_address = models.CharField(max_length=255, blank=True, null=True)
    office_phone = models.CharField(max_length=255, blank=True, null=True)
    # nid_number = models.CharField(max_length=255, blank=True, null=True)
    tin_number = models.CharField(max_length=255, blank=True, null=True)
    doctor_license_number = models.CharField(max_length=255, blank=True, null=True)
    hospital = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    serviceUuid = models.CharField(max_length=255, blank=True, null=True)
    doctor_fee = models.IntegerField(default=0)
    available_for_appointment = models.BooleanField(default=False)
    ##adding assistant
    assistant = models.ForeignKey('Assistant', models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.doctor.username
    #
    # def save(self, args, *kwargs):
    #     super().save(*args, **kwargs)
    #     img = Image.open(self.profile_picture.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_picture.path)


class Lab(models.Model):
    lab = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    lab_name = models.CharField(max_length=255, blank=True, null=True)
    office_phone = models.CharField(max_length=255, blank=True, null=True)
    trade_license_number = models.CharField(max_length=255, blank=True, null=True)
    tin_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.lab.username


class Pharmacy(models.Model):
    pharmacy = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    pharmacy_name = models.CharField(max_length=255, blank=True, null=True)
    # address = models.CharField(max_length=255, blank=True, null=True)
    # phone = models.CharField(max_length=255, blank=True, null=True)
    office_phone = models.CharField(max_length=255, blank=True, null=True)
    # nid_number = models.CharField(max_length=255, blank=True, null=True)
    tin_number = models.CharField(max_length=255, blank=True, null=True)
    trade_license_number = models.CharField(max_length=255, blank=True, null=True)
    license_number = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.pharmacy.username


# class Patient(models.Model):
#     patient = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
#     # nid_number = models.CharField(max_length=255, blank=True, null=True)
#
#     def __str__(self):
#         return self.patient.usernameF


class Assistant(models.Model):
    assistant = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    serviceUuid = models.CharField(max_length=255, blank=True, null=True)
    available_for_appointment = models.BooleanField(default=False)
    booth_location = models.CharField(max_length=255, blank=True, null=True)
    degree = models.CharField(max_length=255, blank=True, null=True)
    tin_number = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.assistant.username

# def create_assistant_instance(sender, instance, created, **kwargs):
#     if created:
#         Assistant.objects.create(assistant=instance)
#         print("Assistant modal created")
#
#
# post_save.connect(create_assistant_instance, sender=User)


class PaymentInfo(models.Model):
    bank_info = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bank_name = models.CharField(max_length=255, blank=True, null=True)
    account_holder_name = models.CharField(max_length=255, blank=True, null=True)
    bank_account_number = models.CharField(max_length=255, blank=True, null=True)
    bank_branch_name = models.CharField(max_length=255, blank=True, null=True)
    bank_swift_code = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.bank_info.username


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    assistant = models.ForeignKey(Assistant, on_delete=models.CASCADE, blank=True, null=True)
    patientUuid = models.CharField(max_length=255, blank=True, null=True)
    serviceUuid = models.CharField(max_length=255, blank=True, null=True)
    assistant_serviceUuid = models.CharField(max_length=255, blank=True, null=True)
    startDateTime = models.CharField(max_length=255, blank=True, null=True)
    endDateTime = models.CharField(max_length=255, blank=True, null=True)
    providers_uuid = models.CharField(max_length=255, blank=True, null=True)
    date = models.CharField(max_length=255, blank=True, null=True)
    video_stream_id = models.CharField(max_length=500, blank=True, null=True)
    patientIdentifier = models.CharField(max_length=255, blank=True, null=True)
    doctor_name = models.CharField(max_length=255, blank=True, null=True)
    patient_name = models.CharField(max_length=255, blank=True, null=True)
    assistant_name = models.CharField(max_length=255, blank=True, null=True, default='default')
    appointment_uuid = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(blank=True, null=True, default=True)
    # doctor_fee = models.CharField(max_length=255, blank=True, null=True)
    doctor_fee = models.IntegerField(default=0)
    speciality = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    local_appointment_start_date_time = models.DateTimeField(blank=True, null=True)
    local_appointment_end_date_time = models.DateTimeField(blank=True, null=True)
    is_completed = models.BooleanField(blank=True, null=True, default=False)

    def __str__(self):
        return f'{self.patient.username} apointment with {self.doctor}'


class VideoStream(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    streeming_key = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.streeming_key


class ProfilePicture(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)

    def __str__(self):
        return self.user.username




class PaymentType(models.Model):
    type_name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.type_name


class AppointmentPayment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name="appointments")
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE, related_name="payment_types")
    amount = models.IntegerField(blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    appointment_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.appointment.patient_name


def create_profile_picture(sender, instance, created, **kwargs):
    if created:
        ProfilePicture.objects.create(user=instance)
        print(f'-----------------------------------------------sender:{sender}, instance-{instance}, created-{created}, kw-{kwargs}')
        # print("Prifile picture modal created")


post_save.connect(create_profile_picture, sender=User)


def create_appointment_payment(sender, instance, created, **kwargs):
    if created:
        cash_payment_type = PaymentType.objects.get(type_name="Bkash")
        # print("create_appointment_payment(): instance", payment_type)
        AppointmentPayment.objects.create(appointment=instance, payment_type=cash_payment_type)
        # print("create_appointment_payment modal created")


post_save.connect(create_appointment_payment, sender=Appointment)


class Prescription(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    pharmacy =  models.ManyToManyField(Pharmacy)
    visit_uuid = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    is_forwarded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    forwarded_at = models.DateTimeField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.patient.username} prescription {self.id}"

class PrescriptionDrug(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, related_name="prescriptions")
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.BooleanField(default=False)
    given_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"

class Laborder(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    lab =  models.ManyToManyField(Lab)
    visit_uuid = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    is_forwarded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    forwarded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.username} laborder {self.id}"


class LaborderList(models.Model):
    laborder = models.ForeignKey(Laborder, on_delete=models.CASCADE, related_name="laborders")
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # status = models.BooleanField(default=False)
    status = models.PositiveIntegerField(default=0)
    given_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.name}"


class Radiologyorder(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    lab =  models.ManyToManyField(Lab)
    visit_uuid = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    is_forwarded = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    forwarded_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.username} radiology_order {self.id}"


class RadiologyorderList(models.Model):
    radiologyorder = models.ForeignKey(Radiologyorder, on_delete=models.CASCADE, related_name="radiologyorders")
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # status = models.BooleanField(default=False)
    status = models.PositiveIntegerField(default=0)
    given_by = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class Preference(models.Model):
    user_notification = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    email_notification = models.BooleanField(default=True, null=True, blank=True)
    phone_notification = models.BooleanField(default=True, null=True, blank=True)
    both_notification = models.BooleanField(default=False, null=True, blank=True)
    no_notification = models.BooleanField(default=False, null=True, blank=True)
    payment_notification = models.BooleanField(default=False, null=True, blank=True)
    appointment_notification = models.BooleanField(default=True, null=True, blank=True)
    forward_notification = models.BooleanField(default=False, null=True, blank=True)


    def __str__(self):
        return f'{self.user_notification.username} notification preference'

def create_preference(sender, instance, created, **kwargs):
    if created:
        Preference.objects.create(user_notification=instance)
        if User.objects.filter(username='default_assistant').exists():
            print('already have')
        else:
            User.objects.create_user(first_name="default", last_name="assistant", username="default_assistant", email="default_assistant@gmail.com", phone_number="123456789", password="Accelx@123456", is_patient=False, is_doctor=False, is_laboratory=False, is_pharmacy=False, is_assistant=True)

        print(f'-----------------------------------------------sender:{sender}, instance-{instance}, created-{created}, kw-{kwargs}')
        # print("Prifile picture modal created")


post_save.connect(create_preference, sender=User)


    
class Service(models.Model):
    user_service = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    durationMins = models.PositiveIntegerField(blank=True, null=True)
    maxAppointmentsLimit = models.PositiveIntegerField(blank=True, null=True)
    startTime = models.TimeField(null=True, blank=True)
    endTime = models.TimeField(null=True, blank=True)
    specialityUuid = models.CharField(max_length=255, blank=True, null=True)
    locationUuid = models.CharField(max_length=255, blank=True, null=True)
    serviceTypes = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return f'{self.name}'


def create_services(sender, instance, created, **kwargs):
    if created:
        if instance.is_doctor == True or instance.is_assistant == True:
            Service.objects.create(user_service=instance)
            print(f'sender:{sender}, instance-{instance}, created-{created}, kw-{kwargs}')


post_save.connect(create_services, sender=User)
