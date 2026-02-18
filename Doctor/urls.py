from django.urls import path
from Doctor import views 
urlpatterns=[
    path('',views.dhome,name="dhome"),
    path('patientview/',views.patientviewdata,name="patientview"),
    path('display_appointment/',views.display_appointment,name="display_appointment"),
    path('approve_appointment/',views.approve_appointment,name="approve_appointment"),
    path('cancel_appointment/',views.cancle_appointment,name="cancel_appointment"),
    path('viewdetails',views.viewdetails,name="viewdetails"),
]