from django.urls import path
from accounts import views

urlpatterns = [
    # path('doctor', views.DoctorDetails.as_view()),
    path('doctor/<int:pk>', views.SingleDoctorDetails.as_view()),

    # path('patient', views.PatientDetails.as_view()),
    # path('patient/<int:pk>', views.SinglePatientDetails.as_view()),

    path('lab', views.LabDetails.as_view()),
    path('lab/<int:pk>', views.SingleLabDetails.as_view()),

    path('phamarcy', views.PharmacyDetails.as_view()),
    path('phamarcy/<int:pk>', views.SinglePharmacyDetails.as_view()),

    #getting all availabe apointment doctor list
    path('appointment_available_doctor', views.AppointmentAvailableDoctor.as_view()),
    path('appointment_available_assistant', views.AppointmentAvailableAssistant.as_view()),
    path('doctor', views.DoctorDetails.as_view()),
    path('doctor/<int:pk>', views.SingleDoctorDetails.as_view()),
    path('patient/<int:pk>', views.SinglePatientDetails.as_view()),

    path('assistant', views.AssistantDetails.as_view()),
    path('assistant_by_user_name', views.AssistantDetailsByUsername.as_view()),
    path('assistant/<int:pk>', views.SingleAssistantDetails.as_view()),


    path('payment_info', views.PaymentInfoDetails.as_view()),
    path('payment_info/<int:pk>', views.SinglePaymentInfoDetails.as_view()),

    path('appointment/', views.AppointmentView.as_view()),
    path('all_patient/', views.AllPatient.as_view()),
    path('all_doctor/', views.AllDoctor.as_view()),
    path('get_all_assistant/', views.AllAssistant.as_view()),
    path('all_appointment/', views.AllAppointment.as_view()),
    # path('update_appointment_status/', views.UpdateAppointmentStatus.as_view()),
    
    #update appointment status
    path('update_appointment_status/<int:pk>', views.UpdateAppointmentStatus.as_view()),
    
    #update appointment competed status
    path('update_appointment_completed_status/<int:pk>', views.UpdateAppointmentCompletedStatusSerializer.as_view()),

    path('all_pharmacy/', views.AllPharmacy.as_view()),
    path('all_lab/', views.AllLab.as_view()),

    path('patient_appointment_list', views.PatientAppointmentList.as_view()),
    
    #patient completed_appointment_list
    path('patient_completed_appointment_list', views.PatientCompletedAppointmentList.as_view()),

    path('doctor_appointment_list', views.DoctorAppointmentList.as_view()),
    #doctor completed_appointment_list
    path('doctor_completed_appointment_list', views.DoctorCompletedAppointmentList.as_view()),
    
    path('assistant_appointment_list', views.AssistantAppointmentList.as_view()),
    #assistant completed_appointment_list
    path('assistant_completed_appointment_list', views.AssistantCompletedAppointmentList.as_view()),

    path('assistant_by_bhamniuuid', views.AssistantByBhamniId.as_view()),
    path('doctor_by_bhamniuuid', views.DoctorByBhamniId.as_view()),
    path('patient_by_bhamniuuid', views.PatientByBhamniId.as_view()),

    path('pharmacy_by_user_id', views.PharmacyByUseriId.as_view()),


    path('profile_picture/<int:pk>', views.ProfilePictureView.as_view()),
    path('profile_picture_by_user_id', views.ProfilePictureByUserId.as_view()),

    path('appointment-list-with-payment', views.AppointmentPaymentListAPIView.as_view()),
    path('appointment-list-with-payment/<int:pk>/', views.AppointmentPaymentCreateUpdateAPIView.as_view()),

    path('singleappointmnet', views.SingleAppointment.as_view()),


    path('prescription/', views.PrescriptionView.as_view()),
    path('prescription_update/<int:pk>', views.UpdatePrescriptionView.as_view()),

    path('prescription_by_visit/', views.PrescriptionByVisitUuidView.as_view()),
    path('prescription_by_pharmacy_id/', views.PrescriptionByPharmacyIdView.as_view()),

    path('prescription_drug/', views.PrescriptionDrugView.as_view()),
    path('prescription_drug_update/<int:pk>', views.UpdatePrescriptionDrugView.as_view()),
    path('prescription_drug_by_prescription_id/', views.PrescriptionDrugByPrescriptionIdView.as_view()),

    path('laborder/', views.LaborderView.as_view()),
    path('laborder_list/', views.LaborderListView.as_view()),
    path('laborder_by_visit/', views.LaborderByVisitUuidView.as_view()),
    path('laborder_by_lab_id/', views.LaborderByLabIdView.as_view()),
    path('laborder_list_by_laborder_id/', views.LaborderListByLabIdView.as_view()),
    path('laborder_update/<int:pk>', views.UpdateLaborderView.as_view()),
    path('laborder_list_update/<int:pk>', views.UpdateLaborderListView.as_view()),

    #Radiologyorder
    path('radiologyorder/', views.RadiologyorderView.as_view()),
    path('radiologyorder_list/', views.RadiologyorderListView.as_view()),
    path('radiologyorder_by_visit/', views.RadiologyorderByVisitUuidView.as_view()),
    path('radiologyorder_by_lab_id/', views.RadiologyorderByLabIdView.as_view()),
    path('radiologyorder_list_by_radiologyorder_id/', views.RadiologyorderListByLabIdView.as_view()),
    path('radiologyorder_update/<int:pk>', views.UpdateRadiologyorderView.as_view()),
    path('radiologyorder_list_update/<int:pk>', views.UpdateRadiologyorderListView.as_view()),

    #Preference
    path('preference', views.PreferenceDetailsByUserId.as_view()),
    path('preference/<int:pk>', views.SinglePreferenceDetails.as_view()),

    #service
    path('service', views.ServiceDetailsByUserId.as_view()),
    path('service/<int:pk>', views.SingleServiceDetails.as_view()),
    


    #doctor complete appointment filter by date
    path('doctor_appointment_filter_by_date', views.DoctorCompletedAppointmentListByDateRange.as_view()),  
    path('assistant_appointment_filter_by_date', views.AssistantCompletedAppointmentListByDateRange.as_view()),  
    path('patient_appointment_filter_by_date', views.PatientCompletedAppointmentListByDateRange.as_view()),  


    path('user_details/', views.UserDetails.as_view()),



]