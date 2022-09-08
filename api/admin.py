from django.contrib import admin
from api.models import Help
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Help)


class HelpAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'id', 'title', 'collaps_id',
                'patient_help','doctor_help','pharmacy_help',
                        'laboratory_help','assistant_help', 'ordering', 'description')


admin.site.register(Help, HelpAdmin)
