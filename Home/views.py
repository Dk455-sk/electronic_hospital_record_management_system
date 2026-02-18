from django.shortcuts import render,HttpResponse
from .models  import Contact_master

# Create your views here.
def home(request):
    return render(request,"home.html")

def gallery(request):
    return render(request,"gallery.html")


def contact(request):
    if request.method=="POST":
        Name=request.POST["name"]
        Email=request.POST["email"]
        Message=request.POST["message"]
        ob=Contact_master.objects.create(name=Name,email=Email,message=Message)
        ob.save()
        return render(request,"contact.html",{'msg':"Register successfull"})

    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")


def index(request):
    return HttpResponse("<h1 >welcome to django world....</h2>")

def  add(request):
    if request.method=="POST":
        a=request.POST['fno']
        b=request.POST['sno']
        result=int(a)+int(b)
        return render(request,"add.html",context={"output":result})

    return render(request,"add.html")

def  calculator(request):
    if request.method=="POST":
        a=request.POST['fno']
        b=request.POST['sno']
        btn=request.POST['btn']
        if btn=="add":
            result=int(a)+int(b)
        elif btn=="sub":
            result=int(a)-int(b)
        elif btn=="mul":
            result=int(a)*int(b)
        else:
            result=int(a)/int(b)
        return render(request,"calculator.html",context={"output":result})
    

    return render(request,"calculator.html")