from django.shortcuts import render
from .models import Register_Master

# Create your views here.
def signup(request):
    if request.method=="POST":
        username=request.POST["name"]
        email=request.POST["email"]
        mobile=request.POST["mobile"]
        password=request.POST["pwd"]
        gender=request.POST["gender"]        
        dob=request.POST["dob"]
        address=request.POST["adds"]
        role_name=request.POST["role"]
        ob=Register_Master.objects.create(Name=username,Email=email,Mobile=mobile,
        Password=password,Dob=dob,Gender=gender,Address=address,Role_name=role_name)
        ob.save()
        return render(request,"signup.html",{'msg':"Register successfull"})


    return render(request,"signup.html")