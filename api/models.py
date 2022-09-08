from django.db import models
from ckeditor.fields import RichTextField

class Help(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    collaps_id = models.CharField(max_length=255, blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    
    patient_help = models.BooleanField(default=False)
    doctor_help = models.BooleanField(default=False)
    laboratory_help = models.BooleanField(default=False)
    pharmacy_help = models.BooleanField(default=False)
    assistant_help = models.BooleanField(default=False)

    ordering = models.IntegerField()

    class Meta:
        order_with_respect_to = 'ordering'

    def __str__(self):
        return self.title

