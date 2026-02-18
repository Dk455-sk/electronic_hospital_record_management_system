from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from REGISTER.models import Register_Master
from Patient.models import Doctor_Appointment
from .models import *
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
# def viewdetails(request):
#     if request.method=="POST":
#         pid=request.POST.get("pid")
#         btn=request.POST.get("btn")
#         if btn=="View Details":
#             ob=Doctor_Appointment.objects.get(id=pid)
#             return render(request,"patient_details.html",{'pdata':ob})
#         elif btn=="Submit":
#             prescription_text=request.POST["prescription"]
#             app=Doctor_Appointment.objects.get(id=pid)

#             Prescription.objects.create(
#                 app_id=app,
#                 prescription_text=prescription_text
#             )
#             return redirect("display_appointment")
#     return redirect("display_appointment")



def logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want to send after logout

def viewdetails(request):
    if request.method == "POST":
        pid = request.POST.get("pid")
        btn = request.POST.get("btn")

        print(f"Received POST: pid={pid}, btn={btn}")  # Debugging line

        if not pid:
            return HttpResponse("Missing pid", status=400)

        if btn == "View Details":
            ob = get_object_or_404(Doctor_Appointment, id=pid)
            return render(request, "patient_details.html", {'pdata': ob})

        elif btn == "Submit":
            prescription_text = request.POST.get("prescription")
            app = get_object_or_404(Doctor_Appointment, id=pid)
 
            Prescription.objects.create(
            app_id=app,
            prescription=prescription_text)
            return redirect("display_appointment")


    return redirect("display_appointment")


def display_appointment(request):
    email=request.session.get("email")
    ob=Register_Master.objects.get(Email=email)
    ob1=Doctor_Appointment.objects.filter(doct_email=ob)
    # ob2=Doctor_Appointment.objects.all()
    return render(request,"appointment_details.html",{"appointment":ob1})

def patientviewdata(request):
    ob=Register_Master.objects.filter(Role_name="patient")
    return render(request,"patientviewdata.html",{'pdata':ob})

def dhome(request):
    dname=request.session.get('name')
    return render(request,"dhome.html",{'Dname':dname})

def approve_appointment(request):
    if request.method=="POST":
        appointment_id=request.POST.get("appointment_id")
        appointment=get_object_or_404(Doctor_Appointment,id=appointment_id)
        appointment.status="Aproved"
        appointment.save()
        messages.success(request,f"Appointment for {appointment.p_name} has been approved.")
        return redirect('display_appointment')
    
def cancle_appointment(request):
    if request.method=="POST":
        appointment_id=request.POST.get("appointment_id")
        appointment=get_object_or_404(Doctor_Appointment,id=appointment_id)
        appointment.status="Cancelled" 
        appointment.save()
        messages.error(request,f"Appointment for {appointment.p_name} has been cancelled.")
        return redirect('display_appointment')
    