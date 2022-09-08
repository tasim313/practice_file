from django.urls import include, path

from .views import *

urlpatterns = [
    path("persion", persionApi, name="person"),
    path("persion_update", personUpdateApi, name="person_update"),
    path("patient", patientApi, name="patient"),
    path("get_radilogy/<patient_uuid>", get_radilogy, name="get_radilogy"),
    path("get-image-report/", get_image_report, name="get_image_report"),
    path("get-ml-report/", GetRadiologyView.as_view(), name="get_ml_report"),
    path("get_prescription/<bahmniuid>", get_prescription, name="get_prescription"),
    path("organization-results/<org_name>", organization_result_view, name="organization_result_view"),
    path("result_update_view/<result_id>/<value>", result_update_view, name="result_update_view"),
    # path("result_update_view/", result_update_view, name="result_update_view"),

    # Appointment related api
    path("find_appointment_schedule_doctor/", find_appointment_schedule_doctor, name="find_appointment_schedule_doctor"),
    path("find_appointment_schedule_assistant/", find_appointment_schedule_assistant, name="find_appointment_schedule_assistant"),


    path("get_appointment_ending_time/", edn_time, name="edn_time"),
    path("all_services/", get_all_services, name="get_all_services"),
    path("get_all_provider/", get_all_provider, name="get_all_provider"),
    path("create_appointment/", create_appointment, name="create_appointment"),

    path("get_all_doctors/", get_all_doctors, name="get_all_doctors"),
    path("get_all_assistant/", get_all_assistant, name="get_all_assistant"),

    #opd vist on
    path("opd_visit_on/", opd_visit_on, name="opd_visit_on"),

    #get all location from bhamni
    path("get_all_location_bhamni/", get_all_location_bhamni, name="get_all_location_bhmani"),
    #get all speciality from bhamni
    path("get_all_speciality_bhamni/", get_all_speciality_bhamni, name="get_all_speciality_bhamni"),


    #creating services in bhamni
    path("create_service_bhamni/", create_service_bhamni, name="create_service_bhamni"),
    #creating services in bhamni
    path("update_service_bhamni/", update_service_bhamni, name="update_service_bhamni"),
    

    # By masuk

    path("get_patient_visit_list/<patient_uuid>", get_patient_visit_list, name="get_patient_visit_list"),
    path("get_visit_medication_details/<patient_uuid>/<visit_uuid>", get_visit_medication_details, name="get_visit_medication_details"),
    path("cancle_appointment/<bahmni_appointment_id>/", cancle_appointment, name="cancle_appointment"),

    #Help section
    path("help/", HelpListApiView.as_view(), name="help"),
]
