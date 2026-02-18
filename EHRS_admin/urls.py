from django.urls import path
from EHRS_admin import views
urlpatterns=[
    path('',views.ahome,name="ahome"),
    path('viewdata/',views.viewdata,name="viewdata"),
    path('update/',views.update,name="update"),
    path('adminprofile/',views.adminprofile,name="adminprofile"),
    path('adminviewprofile/',views.adminviewprofile,name="adminviewprofile"),
    path('recent-registrations/', views.recent_registrations, name='recent_registrations'),
]