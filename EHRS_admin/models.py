from django.db import models
from REGISTER.models import Register_Master
# Create your models here.
class adminprofile_master(models.Model):
    email=models.ForeignKey(Register_Master,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to='Image/')
    Document=models.FileField(upload_to="Document/")
    def __str__(self):
        return f'{self.email}'
    

