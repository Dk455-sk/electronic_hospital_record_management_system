from django.urls import path
from Patient import views 
urlpatterns=[
    path('',views.phome,name="phome"),
    path('doctorview/',views.doctorview,name="doctorview"),
    path('take_appointment',views.take_appointment,name="take_appointment"),
    path('success',views.success, name="success"),
    path('patient_dashboard',views.patient_dashboard,name="patient_dashboard"),
    path('test_view',views.test_view,name="test_view"),
    path('test_report',views.test_report,name="test_report")
]