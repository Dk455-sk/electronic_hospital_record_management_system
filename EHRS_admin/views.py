from django.shortcuts import render,redirect
from REGISTER.models import Register_Master
from .models import *
from django.db.models import Sum
from django.utils.timezone import now
from datetime import date
from django.contrib.auth import logout
# Create your views here.
# def adminviewprofile(request):
#     email=request.session.get('email')
#     ob=Register_Master.objects.get(Email=email)
#     obj=adminprofile_master.objects.get(email=ob)
#     return render(request,'adminviewprofile.html',{'data':ob,"data1":obj})

def logout_view(request):
    logout(request)
    return redirect('home')
def adminviewprofile(request):
    email = request.session.get('email')
    ob = Register_Master.objects.get(Email=email)
    
    try:
        obj = adminprofile_master.objects.get(email=ob)
    except adminprofile_master.DoesNotExist:
        obj = None  # no profile yet

    return render(request, 'adminviewprofile.html', {'data': ob, 'data1': obj})



def adminprofile(request):
    email=request.session.get('email')
    ob=Register_Master.objects.get(Email=email)
    if request.method=="POST":
        image_file=request.FILES["image"]
        document=request.FILES["upload_doc"]
        profile_update_obj,created=adminprofile_master.objects.get_or_create(email=ob)
        if image_file:
            profile_update_obj.Image=image_file
        if document:
            profile_update_obj.Document=document
        profile_update_obj.save()

        ob.Name=request.POST.get('name',ob.Name)
        ob.Email=request.POST.get('email',ob.Email)
        ob.Mobile=request.POST.get('mob',ob.Mobile)
        ob.Gender=request.POST.get('gender',ob.Gender)
        ob.Role_name=request.POST.get('role',ob.Role_name)
        ob.Dob=request.POST.get('dob',ob.Dob)
        ob.save()

        return redirect("adminprofile")
        
    return render(request,"adminprofile.html",{'user':ob})




def viewdata(request):
    ob=Register_Master.objects.all()
    if request.method=="POST":
        email=request.POST["email"]
        btn=request.POST["btn"]

        if btn=="Delete":
            Register_Master.objects.get(Email=email).delete()
            return redirect("viewdata")
        elif btn=="Edit":
            ob=Register_Master.objects.get(Email=email)
            return render(request,"edit.html",{'user':ob})
        
    return render(request,"viewdata.html",{'data':ob})

def update(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        gender=request.POST["gender"]
        Dob=request.POST["dob"]
        mob=request.POST["mob"]
        status=request.POST["status"]
        ob=Register_Master.objects.filter(Email=email).update(Name=name,Gender=gender,Dob=Dob,Mobile=mob,Status=status)

        return redirect("viewdata")
    return render(request,"viewdata.html")


def ahome(request):
    aname=request.session.get('name')
    return render(request,"ahome.html",{'Aname':aname})


def recent_registrations(request):
    # Get optional role filter from query parameters
    role_filter = request.GET.get("role")  # 'doctor', 'patient', 'staff', or None

    if role_filter:
        # If role is selected, show all users of that role ordered by registration
        recent_users = Register_Master.objects.filter(Role_name=role_filter).order_by('-created_at')
    else:
        # Otherwise, show the 10 most recent registrations
        recent_users = Register_Master.objects.all().order_by('-created_at')[:10]

    # Count by role for the dashboard cards
    total_doctors = Register_Master.objects.filter(Role_name="doctor").count()
    total_patients = Register_Master.objects.filter(Role_name="patient").count()
    total_staff = Register_Master.objects.filter(Role_name="staff").count()

    context = {
        "Aname": request.session.get('name'),  # Admin name from session
        "recent_users": recent_users,
        "total_doctors": total_doctors,
        "total_patients": total_patients,
        "total_staff": total_staff,
        "role_filter": role_filter,
    }

    return render(request, "admin_recent_registrations.html", context)