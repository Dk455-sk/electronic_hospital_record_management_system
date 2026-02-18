from django.db import models

# Create your models here.

class Laboratory_test(models.Model):
    test_id=models.AutoField(primary_key=True)
    test_name=models.CharField(max_length=40)
    test_price=models.IntegerField(default=10)


class Bill(models.Model):
    patient = models.ForeignKey('REGISTER.Register_Master', on_delete=models.CASCADE)
    consultation = models.FloatField(default=0)
    lab_tests = models.FloatField(default=0)
    medication = models.FloatField(default=0)
    room = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    subtotal = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    total = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient.Name} (ID: {self.patient.Reg_id}) on {self.created_at.strftime('%d-%m-%Y')}"
