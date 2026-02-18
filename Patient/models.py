from django.db import models
from REGISTER.models  import Register_Master
from datetime import date,time
from Staff.models import Laboratory_test
# Create your models here.
class PatientTestReport(models.Model):
    report_id = models.AutoField (primary_key=True)
    patient = models. ForeignKey (Register_Master, on_delete=models.CASCADE)
    tests = models. ManyToManyField (Laboratory_test)
    total_price = models. DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField (auto_now_add=True)
    def __str__(self):
        return f"Report{self.report_id} - {self.patient.Name}"

class Doctor_Appointment(models.Model):
    id=models.AutoField(primary_key=True)
    doct_name=models.CharField(max_length=60)
    doct_contact=models.CharField(max_length=15)
    doct_email=models.ForeignKey(Register_Master,on_delete=models.CASCADE)
    # P_email=models.ForeignKey(Register_Master,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=100)
    p_mobile=models.CharField(max_length=15)
    p_address=models.TextField()
    p_gender=models.CharField(max_length=15)
    dob=models.DateField()
    p_disease=models.CharField(max_length=255)
    todaydate=models.DateField(auto_now=True)
    a_date=models.DateField(default=date.today)
    fromtime=models.TimeField(default=time(9,0))
    totime=models.TimeField(default=time(17,0))
    status=models.CharField(max_length=30,default="pending")
    
    def __str__(self):
        return self.doct_name
    
    
