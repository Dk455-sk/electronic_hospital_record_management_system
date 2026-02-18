"""
URL configuration for EHRS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Home import views as hviews
from REGISTER import views as rviews
from Login import views as lviews
from django.conf import settings
from django.conf.urls.static import static
from Doctor import views as dviews
from Patient import views as pviews
from Staff import views as sviews
from EHRS_admin import views as aviews 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',lviews.login,name="signin"),
    path('signup/',rviews.signup,name="signup"),
    path('logout/', dviews.logout_view, name='logout'),
    path('logout/', pviews.logout_view, name='logout'),
    path('logout/', sviews.logout_view, name='logout'),
    path('logout/', aviews.logout_view, name='logout'),
    path('',hviews.home,name="home"),
    path("xyz",hviews.index,name="xyz"),
    path("gallery",hviews.gallery,name="gallery"),
    path("contact",hviews.contact,name="contact"),
    path("about",hviews.about,name="about"),
    # path("doctor",dviews.dhome,name="doctor"),
    # path('staff',sviews.shome,name="staff"),
    # path('ehrs_admin',aviews.ahome,name="ehrs_admin"),
    # path('patient',pviews.phome,name="patient"),
    
    #doctor
    path('doctor/',include('Doctor.urls')),
    #patient
    path('patient/',include('Patient.urls')),
    #staff
    path('staff/',include('Staff.urls')),
    #ehrs_admin
    path('ehrs_admin/',include('EHRS_admin.urls')),

    
    path("add",hviews.add,name="add"),
    path("calculator",hviews.calculator,name="calculator")

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)