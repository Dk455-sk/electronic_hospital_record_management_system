from django.db import models
from Patient.models import *
# Create your models here.
class Prescription(models.Model):
    pres_id=models.AutoField(primary_key=True)
    app_id=models.ForeignKey(Doctor_Appointment,on_delete=models.CASCADE)
    prescription=models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription {self.pres_id} for Appointment {self.app_id}"
    
    
