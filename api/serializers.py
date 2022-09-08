from django.db.models import fields
from rest_framework import serializers
from .models import Help



class HelpSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ['id', 'title', 'collaps_id', 
                    'patient_help','doctor_help','pharmacy_help',
                        'laboratory_help', 'assistant_help', 'ordering', 'description']
