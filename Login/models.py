from django.db import models

# Create your models here.
class Register_Master(models.Model):
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=40)
    def __str__(self):
        return self.Name