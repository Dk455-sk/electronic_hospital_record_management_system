from django.urls import path
from Staff import views
urlpatterns=[
    path('',views.shome,name="shome"),
    path('pdview/',views.patient_doctor_view,name="pdview"),
    path('add_test',views.add_test,name="add_test"),
    path('billing',views.generate_bill,name="billing"),
    path('bill_records/', views.bill_records, name='bill_records'),
    path('cancel_bill/<int:bill_id>/', views.cancel_bill, name='cancel_bill'), 
    path('applytest',views.applytest,name="applytest"),
]