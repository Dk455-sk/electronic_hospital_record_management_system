from django.contrib import admin
from .models import Register_Master

# Register your models here.from .models import Register_Master
admin.site.register(Register_Master)

#python manage.py makemigrations
#python manage.py migrate
#python manage.py createsuperuser
#username=admin
#password=admin

