from django.contrib import admin
from .models import Laboratory_test
from .models import Bill
# Register your models here.
# admin.site.register(Laboratory_test)
admin.site.register(Bill)






class changetest(admin.ModelAdmin):
    fields=['test_price','test_name']
    search_fields=["test_name"]
    list_filter=['test_price',"test_name"]
    list_display=['test_price',"test_name"]
    list_editable=['test_name']

admin.site.register(Laboratory_test,changetest)

