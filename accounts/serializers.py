from django.db.models import fields
from django.db import models
from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Doctor, Pharmacy, Lab, Assistant, PaymentInfo, Appointment, ProfilePicture, PaymentType, AppointmentPayment, Prescription, PrescriptionDrug, Laborder, LaborderList, Radiologyorder, RadiologyorderList, Preference, Service

User = get_user_model()


class CustomSerializer(serializers.HyperlinkedModelSerializer):

    def get_field_names(self, declared_fields, info):
        expanded_fields = super(CustomSerializer, self).get_field_names(declared_fields, info)

        if getattr(self.Meta, 'extra_fields', None):
            return expanded_fields + self.Meta.extra_fields
        else:
            return expanded_fields

class CustomUserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'is_admin', 'is_staff',
                  'is_patient', 'is_doctor', 'is_laboratory', 'is_pharmacy', 'is_assistant', 'phone_number', 'address', 'gender',
                  'date_of_birth', 'country', 'state', 'city', 'postal_code', 'nid_number', 'identifier', 'bhamniuuid', "account_created"]



class PreferenceSerializer(serializers.ModelSerializer):
    """
    Preference modal serializer
    """

    user_preference = CustomUserSerialiser(read_only=True, source='preference')

    class Meta:
        model = Preference
        fields = '__all__'
        extra_fields = ['user_preference']

class DoctorUserSerializer(serializers.ModelSerializer):
    """
    doctor modal serializer
    """
    user_doctor = CustomUserSerialiser(read_only=True, source='doctor')

    class Meta:
        model = Doctor
        fields = '__all__'
        extra_fields = ['user_doctor']




class PharmacyUserSerializer(serializers.ModelSerializer):
    """
    doctor modal serializer
    """

    user_pharmacy = CustomUserSerialiser(read_only=True, source='pharmacy')

    class Meta:
        model = Pharmacy
        fields = '__all__'
        extra_fields = ['user_pharmacy']




class LabUserSerializer(serializers.ModelSerializer):
    """
    doctor modal serializer
    """
    user_lab = CustomUserSerialiser(read_only=True, source='lab')

    class Meta:
        model = Lab
        fields = '__all__'
        extra_fields = ['user_lab']




# class PatientUserSerializer(serializers.ModelSerializer):
#     """
#     doctor modal serializer
#     """
#
#     class Meta:
#         model = Patient
#         fields = '__all__'


class AssistantUserSerializer(serializers.ModelSerializer):
    """
    doctor modal serializer
    """
    user_assistant = CustomUserSerialiser(read_only=True, source='assistant')

    class Meta:
        model = Assistant
        fields = '__all__'
        extra_fields = ['user_assistant']



class PaymentInfoSerializer(serializers.ModelSerializer):
    """
    doctor modal serializer
    """

    class Meta:
        model = PaymentInfo
        fields = '__all__'


class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    """
    appointment modal serializer
    """
    class Meta:
        model = Appointment
        fields = '__all__'



class AppointmentStatusSerializer(serializers.ModelSerializer):
    """
    appointment status modal serializer
    """

    class Meta:
        model = Appointment
        fields = ['id', 'status']


class AppointmentCompletedStatusSerializer(serializers.ModelSerializer):
    """
    appointment completed status modal serializer
    """

    class Meta:
        model = Appointment
        fields = ['id', 'is_completed']



class PaymentTypeSerializer(serializers.ModelSerializer):
    """"
     Serialiser for payment type
    """

    class Meta:
        model = PaymentType
        fields = '__all__'


class AppointmentPaymentSerializer(serializers.ModelSerializer):
    """"
     Serialiser for payment type
    """
    appointment = AppointmentSerializer()
    payment_type = PaymentTypeSerializer()

    class Meta:
        model = AppointmentPayment
        fields = ["id", "amount", "transaction_id", "appointment_status", "created_at", "updated_at", "appointment", "payment_type"]


class AppointmentPaymentCRUDSerializer(serializers.ModelSerializer):
    """"
     Serialiser for payment type CREATE, UPDATE, READ
    """

    class Meta:
        model = AppointmentPayment
        fields = ["id", "amount", "transaction_id", "appointment_status", "created_at", "updated_at", "appointment", "payment_type"]



class PrescriptionSerializer(serializers.ModelSerializer):
    """"
     Serialiser for prescription
    """
    class Meta:
        model = Prescription
        fields = ["id", "patient", "pharmacy", "visit_uuid", "status", "is_forwarded" ,"created_at", "updated_at", "forwarded_at"]


class PrescriptionDrugSerializer(serializers.ModelSerializer):
    """"
     Serialiser for prescription drug
    """

    user_prescription = PrescriptionSerializer(read_only=True, source='prescription')
    class Meta:
        model = PrescriptionDrug
        fields = ["id", "prescription", "name", "description", "status", "given_by", "created_at", "updated_at", 'user_prescription']


class LaborderSerializer(serializers.ModelSerializer):
    """"
     Serialiser for Laborder
    """
    class Meta:
        model = Laborder
        fields = ["id", "patient", "lab", "visit_uuid", "status", "is_forwarded" ,"created_at", "updated_at", "forwarded_at"]


class LaborderListSerializer(serializers.ModelSerializer):
    """"
     Serialiser for Laborder List
    """

    user_lab_order = LaborderSerializer(read_only=True, source='laborder')
    class Meta:
        model = LaborderList
        fields = ["id", "laborder", "name", "description", "status", "given_by", "created_at", "updated_at", 'user_lab_order']




class RadiologyorderSerializer(serializers.ModelSerializer):
    """"
     Serialiser for Radiologyorder
    """
    class Meta:
        model = Radiologyorder
        fields = ["id", "patient", "lab", "visit_uuid", "status", "is_forwarded" ,"created_at", "updated_at", "forwarded_at"]


class RadiologyorderListSerializer(serializers.ModelSerializer):
    """"
     Serialiser for Radiologyorder List
    """

    user_radiology_order = RadiologyorderSerializer(read_only=True, source='radiologyorder')
    class Meta:
        model = RadiologyorderList
        fields = ["id", "radiologyorder", "name", "description", "status", "given_by", "created_at", "updated_at", 'user_radiology_order']



class ServiceSerializer(serializers.ModelSerializer):
    """
    Service modal serializer
    """
    user_service = CustomUserSerialiser(read_only=True, source='service')
    class Meta:
        model = Service
        fields = '__all__'
        extra_fields = ['user_service']