from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from accounts.models import Service, User, Doctor, Pharmacy, Lab, PaymentInfo, Appointment, Assistant, VideoStream, \
    ProfilePicture, PaymentType, AppointmentPayment, Prescription, PrescriptionDrug, Pharmacy, Laborder, LaborderList, Radiologyorder, RadiologyorderList, Preference

# admin.site.register(User)
# admin.site.register(Doctor)
# admin.site.register(Pharmacy)
# admin.site.register(Patient)
# admin.site.register(Lab)
# admin.site.register(PaymentInfo)
# admin.site.register(Appointment)
# admin.site.register(Assistant)


# admin.site.register(VideoStream)
# admin.site.register(ProfilePicture)
# admin.site.register(Prescription)
# admin.site.register(PrescriptionDrug)


class DoctorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'doctor', 'degree', 'specialist', 'hospital',)


admin.site.register(Doctor, DoctorAdmin)


class AssistantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'assistant', 'booth_location',)


admin.site.register(Assistant, AssistantAdmin)


class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'email', 'username', 'bhamniuuid', 'account_created', 'is_patient', 'is_doctor', 'is_assistant')


admin.site.register(User, UserAdmin)


class AppointmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'doctor', 'assistant', 'doctor_name', 'patient_name', 'startDateTime')


admin.site.register(Appointment, AppointmentAdmin)


class ProfilePictureAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'profile_picture')

admin.site.register(ProfilePicture, ProfilePictureAdmin)

class PaymentTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('type_name', 'create_at')

admin.site.register(PaymentType, PaymentTypeAdmin)


class AppointmentPaymentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('appointment', 'payment_type', 'amount', 'transaction_id', 'appointment_status', 'created_at', 'updated_at')

admin.site.register(AppointmentPayment, AppointmentPaymentAdmin)



class PrescriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'patient', 'created_at', 'updated_at', 'forwarded_at' )

admin.site.register(Prescription, PrescriptionAdmin)



class PharmacyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'pharmacy', 'pharmacy_name', 'office_phone')

admin.site.register(Pharmacy, PharmacyAdmin)


class PrescriptionDrugAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'prescription', 'description', 'status', 'given_by')

admin.site.register(PrescriptionDrug, PrescriptionDrugAdmin)


class LabAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'lab', 'lab_name', 'office_phone', 'trade_license_number', 'tin_number', 'description')

admin.site.register(Lab, LabAdmin)

class LaborderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'patient', 'created_at', 'updated_at', 'forwarded_at' )

admin.site.register(Laborder, LaborderAdmin)


class LaborderListAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'laborder', 'description', 'status', 'given_by')

admin.site.register(LaborderList, LaborderListAdmin)


class RadiologyorderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'patient', 'created_at', 'updated_at', 'forwarded_at' )

admin.site.register(Radiologyorder, RadiologyorderAdmin)


class RadiologyorderListAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'radiologyorder', 'description', 'status', 'given_by')

admin.site.register(RadiologyorderList, RadiologyorderListAdmin)


class PaymentInfoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'bank_info', 'bank_name', 'account_holder_name', 'bank_account_number', 'bank_branch_name', 'bank_swift_code')

admin.site.register(PaymentInfo, PaymentInfoAdmin)


class PreferenceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'user_notification', 'email_notification', 'phone_notification', 'both_notification', 'no_notification', 'payment_notification', 'appointment_notification', 'forward_notification')

admin.site.register(Preference, PreferenceAdmin)


class ServiceAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'user_service', 'name')

admin.site.register(Service, ServiceAdmin)
