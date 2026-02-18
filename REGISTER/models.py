from django.db import models
from django.utils import timezone
# Create your models here.
class Register_Master(models.Model):
    Reg_id=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=30,unique=True)
    Mobile=models.CharField(max_length=30)
    Password=models.CharField(max_length=40)
    Dob=models.DateField()
    Gender=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    Role_name=models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.Name}-{self.Role_name}"
