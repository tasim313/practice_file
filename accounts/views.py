import json

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
import datetime

from .models import User, Doctor, Service, Lab, Pharmacy, Assistant, PaymentInfo, Appointment, ProfilePicture, AppointmentPayment, Prescription, PrescriptionDrug, Laborder, LaborderList, Radiologyorder, RadiologyorderList, Preference
from .serializers import DoctorUserSerializer, LabUserSerializer, PharmacyUserSerializer, \
    AssistantUserSerializer, PaymentInfoSerializer, AppointmentSerializer, CustomUserSerialiser, \
    ProfilePictureSerializer, AppointmentStatusSerializer, AppointmentPaymentSerializer, \
    AppointmentPaymentCRUDSerializer, PrescriptionSerializer, PrescriptionDrugSerializer, PharmacyUserSerializer, LaborderSerializer, LaborderListSerializer, RadiologyorderSerializer, RadiologyorderListSerializer, PreferenceSerializer, \
    AppointmentCompletedStatusSerializer, ServiceSerializer

# Create your views here.
class DoctorDetails(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorUserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = Doctor.objects.all()
        if id is not None:
            queryset = queryset.filter(doctor__id=id)
        return queryset


# getting all availabe apointment doctor list
class AppointmentAvailableDoctor(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Doctor.objects.all().filter(available_for_appointment=True)
    serializer_class = DoctorUserSerializer

    def get(self, request):
        return self.list(request)


class AppointmentAvailableAssistant(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Assistant.objects.all().filter(available_for_appointment=True)
    serializer_class = AssistantUserSerializer

    def get(self, request):
        return self.list(request)

    # def post(self, request):
    #     return self.create(request)
    #
    # def get_queryset(self):
    #     id = self.request.query_params.get('id')
    #     queryset = Doctor.objects.all()
    #     if id is not None:
    #         queryset = queryset.filter(doctor__id=id)
    #     return queryset


class SingleDoctorDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorUserSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)


# class PatientDetails(generics.GenericAPIView, mixins.CreateModelMixin):
#     queryset = Patient.objects.all()
#     serializer_class = PatientUserSerializer
#
#     def post(self, request):
#         return self.create(request)
#
#

class SinglePatientDetails(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = User.objects.all().filter(is_patient=True)
    serializer_class = CustomUserSerialiser

    def get(self, request, pk):
        return self.retrieve(request, pk)


class LabDetails(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Lab.objects.all()
    serializer_class = LabUserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = Lab.objects.all()
        if id is not None:
            queryset = queryset.filter(lab__id=id)
        return queryset


class SingleLabDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    queryset = Lab.objects.all()
    serializer_class = LabUserSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)


class PharmacyDetails(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyUserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = Pharmacy.objects.all()
        if id is not None:
            queryset = queryset.filter(pharmacy__id=id)
        return queryset


class SinglePharmacyDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyUserSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)


class AssistantDetails(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Assistant.objects.all()
    serializer_class = AssistantUserSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = Assistant.objects.all()
        if id is not None:
            queryset = queryset.filter(assistant__id=id)
        return queryset

class AssistantDetailsByUsername(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Assistant.objects.all()
    serializer_class = AssistantUserSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        username = self.request.query_params.get('username')
        queryset = Assistant.objects.all()
        if username is not None:
            queryset = queryset.filter(assistant_username=username)
        return queryset



class SingleAssistantDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin):
    queryset = Assistant.objects.all()
    serializer_class = AssistantUserSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)


class PaymentInfoDetails(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = PaymentInfo.objects.all()
        if id is not None:
            queryset = queryset.filter(bank_info__id=id)
        return queryset


class SinglePaymentInfoDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                               mixins.DestroyModelMixin):
    queryset = PaymentInfo.objects.all()
    serializer_class = PaymentInfoSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)


class AppointmentView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class AllPatient(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.filter(is_patient=True, account_created=True)
    serializer_class = CustomUserSerialiser

    def get(self, request):
        return self.list(request)


class AllDoctor(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Doctor.objects.filter(doctor__is_doctor=True)
    serializer_class = DoctorUserSerializer

    def get(self, request):
        return self.list(request)

class AllPharmacy(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Pharmacy.objects.filter(pharmacy__is_pharmacy=True)
    serializer_class = PharmacyUserSerializer

    def get(self, request):
        return self.list(request)


class AllAssistant(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Assistant.objects.filter(assistant__is_assistant=True)
    serializer_class = AssistantUserSerializer

    def get(self, request):
        return self.list(request)


class AllLab(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Lab.objects.filter(lab__is_laboratory=True)
    serializer_class = LabUserSerializer

    def get(self, request):
        return self.list(request)



# class PatientAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
#     queryset = Appointment.objects.all()
#     serializer_class = AppointmentSerializer

#     def get_queryset(self):
#         id = self.request.query_params.get('id')
#         queryset = Appointment.objects.filter(is_completed=False).all()
#         print('queryset', queryset)
#         if id is not None:
#             queryset = queryset.filter(patient=id)
#         return queryset

# getting patient appointment
class PatientAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__patient_id=id, appointment__is_completed=False).order_by('appointment__local_appointment_start_date_time')
        return queryset
# getting all completed patient appointment
class PatientCompletedAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__patient_id=id, appointment__is_completed=True).order_by('-appointment__local_appointment_start_date_time')
        return queryset


class DoctorAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__doctor_id=id, appointment__is_completed=False).order_by('appointment__local_appointment_start_date_time')
        return queryset

#getting all completed appointment of doctor
class DoctorCompletedAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__doctor_id=id, appointment__is_completed=True).order_by('-appointment__local_appointment_start_date_time')
        return queryset


class AssistantAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__assistant_id=id, appointment__is_completed=False).order_by('appointment__local_appointment_start_date_time')
        return queryset


class AssistantCompletedAppointmentList(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__assistant_id=id, appointment__is_completed=True).order_by('-appointment__local_appointment_start_date_time')
        return queryset


class DoctorByBhamniId(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Doctor.objects.all()
    serializer_class = DoctorUserSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        bhamniuuid = self.request.query_params.get('bhamniuuid')
        queryset = Doctor.objects.all()
        if bhamniuuid is not None:
            queryset = queryset.filter(doctor__bhamniuuid=bhamniuuid)
        return queryset


class AssistantByBhamniId(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Assistant.objects.all()
    serializer_class = AssistantUserSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        bhamniuuid = self.request.query_params.get('bhamniuuid')
        queryset = Assistant.objects.all()
        if bhamniuuid is not None:
            queryset = queryset.filter(assistant__bhamniuuid=bhamniuuid)
        return queryset


class PatientByBhamniId(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        bhamniuuid = self.request.query_params.get('bhamniuuid')
        queryset = User.objects.all().filter(is_patient=True)
        if bhamniuuid is not None:
            queryset = queryset.filter(bhamniuuid=bhamniuuid)
        return queryset


class ProfilePictureView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# class ProfilePictureView(APIView):
#     def post(self, request):
#         serializer = ProfilePictureSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     def get(self, request):
#         data = ProfilePicture.objects.all()
#         serializer=ProfilePictureSerializer(data, many=True)
#         return Response(serializer.data)


class ProfilePictureView(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)


class ProfilePictureByUserId(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = ProfilePicture.objects.all()
    serializer_class = ProfilePictureSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = ProfilePicture.objects.all()
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
        return queryset


class AllAppointment(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get(self, request):
        return self.list(request)


class UpdateAppointmentStatus(generics.GenericAPIView, mixins.UpdateModelMixin, ):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentStatusSerializer

    def put(self, request, pk):
        return self.update(request, pk)

#update appointment completed or not
class UpdateAppointmentCompletedStatusSerializer(generics.GenericAPIView, mixins.UpdateModelMixin, ):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentCompletedStatusSerializer

    def put(self, request, pk):
        return self.update(request, pk)


class AppointmentPaymentListAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        appointment_status = self.request.query_params.get('appointment_status')
        queryset = AppointmentPayment.objects.all()
        if appointment_status is not None:
            queryset = queryset.filter(appointment_status=appointment_status)
        return queryset


class AppointmentPaymentCreateUpdateAPIView(
    generics.RetrieveUpdateAPIView):
    queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentCRUDSerializer


class SingleAppointment(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = Appointment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment_uuid=id)
        return queryset


class PrescriptionView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class LaborderView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Laborder.objects.all()
    serializer_class = LaborderSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UpdatePrescriptionView(generics.RetrieveUpdateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class UpdateLaborderView(generics.RetrieveUpdateAPIView):
    queryset = Laborder.objects.all()
    serializer_class = LaborderSerializer

class PrescriptionDrugView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = PrescriptionDrug.objects.all()
    serializer_class = PrescriptionDrugSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class LaborderListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = LaborderList.objects.all()
    serializer_class = LaborderListSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class UpdatePrescriptionDrugView(generics.RetrieveUpdateAPIView):
    queryset = PrescriptionDrug.objects.all()
    serializer_class = PrescriptionDrugSerializer


class UpdateLaborderListView(generics.RetrieveUpdateAPIView):
    queryset = LaborderList.objects.all()
    serializer_class = LaborderListSerializer


class PrescriptionByVisitUuidView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        # patient = self.request.query_params.get('patient')
        visit_uuid = self.request.query_params.get('visit_uuid')
        queryset = Prescription.objects.all()
        if visit_uuid is not None:
            queryset = queryset.filter(visit_uuid=visit_uuid)
        return queryset


class LaborderByVisitUuidView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Laborder.objects.all()
    serializer_class = LaborderSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        # patient = self.request.query_params.get('patient')
        visit_uuid = self.request.query_params.get('visit_uuid')
        queryset = Laborder.objects.all()
        if visit_uuid is not None:
            queryset = queryset.filter(visit_uuid=visit_uuid)
        return queryset



class PrescriptionByPharmacyIdView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        # patient = self.request.query_params.get('patient')
        pharmacy_id = self.request.query_params.get('pharmacy_id')
        queryset = Prescription.objects.all()
        if pharmacy_id is not None:
            queryset = queryset.filter(pharmacy=pharmacy_id)
        return queryset


class LaborderByLabIdView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Laborder.objects.all()
    serializer_class = LaborderSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        lab_id = self.request.query_params.get('lab_id')
        queryset = Laborder.objects.all()
        if lab_id is not None:
            queryset = queryset.filter(lab=lab_id)
        return queryset

class PharmacyByUseriId(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacyUserSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Pharmacy.objects.all()
        if user_id is not None:
            queryset = queryset.filter(pharmacy=user_id)
        return queryset


class UserDetails(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = CustomUserSerialiser

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        queryset = User.objects.all()
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class PrescriptionDrugByPrescriptionIdView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = PrescriptionDrug.objects.all()
    serializer_class = PrescriptionDrugSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        prescription_id = self.request.query_params.get('prescription_id')
        queryset = PrescriptionDrug.objects.all()
        if prescription_id is not None:
            queryset = queryset.filter(prescription=prescription_id)
        return queryset

class LaborderListByLabIdView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = LaborderList.objects.all()
    serializer_class = LaborderListSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        laborder_id = self.request.query_params.get('laborder_id')
        queryset = LaborderList.objects.all()
        if laborder_id is not None:
            queryset = queryset.filter(laborder=laborder_id)
        return queryset


#rediology order Radiologyorder

class RadiologyorderView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Radiologyorder.objects.all()
    serializer_class = RadiologyorderSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class UpdateRadiologyorderView(generics.RetrieveUpdateAPIView):
    queryset = Radiologyorder.objects.all()
    serializer_class = RadiologyorderSerializer



class RadiologyorderListView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = RadiologyorderList.objects.all()
    serializer_class = RadiologyorderListSerializer
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class UpdateRadiologyorderListView(generics.RetrieveUpdateAPIView):
    queryset = RadiologyorderList.objects.all()
    serializer_class = RadiologyorderListSerializer


class RadiologyorderByVisitUuidView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Radiologyorder.objects.all()
    serializer_class = RadiologyorderSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        # patient = self.request.query_params.get('patient')
        visit_uuid = self.request.query_params.get('visit_uuid')
        queryset = Radiologyorder.objects.all()
        if visit_uuid is not None:
            queryset = queryset.filter(visit_uuid=visit_uuid)
        return queryset

class RadiologyorderByLabIdView(generics.GenericAPIView, mixins.ListModelMixin):
    queryset = Radiologyorder.objects.all()
    serializer_class = RadiologyorderSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        lab_id = self.request.query_params.get('lab_id')
        queryset = Radiologyorder.objects.all()
        if lab_id is not None:
            queryset = queryset.filter(lab=lab_id)
        return queryset

class RadiologyorderListByLabIdView(generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = RadiologyorderList.objects.all()
    serializer_class = RadiologyorderListSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        radiologyorder_id = self.request.query_params.get('radiologyorder_id')
        queryset = RadiologyorderList.objects.all()
        if radiologyorder_id is not None:
            queryset = queryset.filter(radiologyorder=radiologyorder_id)
        return queryset

class SinglePreferenceDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

class PreferenceDetailsByUserId(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = Preference.objects.all()
    serializer_class = PreferenceSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Preference.objects.all()
        if id is not None:
            queryset = queryset.filter(user_notification__id=user_id)
        return queryset


class DoctorCompletedAppointmentListByDateRange(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        print('start_date', start_date)
        print('end_date',end_date)
        queryset = AppointmentPayment.objects.all()
        if id and start_date and end_date is not None:
            queryset = queryset.filter(appointment__doctor_id=id, appointment__is_completed=True, appointment__local_appointment_start_date_time__date__range=[start_date, end_date]).order_by('appointment__local_appointment_start_date_time')
            print(queryset)
        return queryset


class AssistantCompletedAppointmentListByDateRange(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__assistant_id=id, appointment__is_completed=True, appointment__local_appointment_start_date_time__date__range=[start_date, end_date]).order_by('appointment__local_appointment_start_date_time')
        return queryset

class PatientCompletedAppointmentListByDateRange(generics.GenericAPIView, mixins.ListModelMixin):
    # queryset = AppointmentPayment.objects.all()
    serializer_class = AppointmentPaymentSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        id = self.request.query_params.get('id')
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        queryset = AppointmentPayment.objects.all()
        if id is not None:
            queryset = queryset.filter(appointment__patient_id=id, appointment__is_completed=True, appointment__local_appointment_start_date_time__date__range=[start_date, end_date]).order_by('appointment__local_appointment_start_date_time')
        return queryset



class SingleServiceDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

class ServiceDetailsByUserId(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ServiceSerializer

    def get(self, request):
        return self.list(request)

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        queryset = Service.objects.all()
        if id is not None:
            queryset = queryset.filter(user_service__id=user_id)
        return queryset
  


    