from django.shortcuts import render,redirect
from REGISTER.models import Register_Master
from Staff.models import Laboratory_test
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth import logout
# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')  # or wherever you want to send after logout

def test_report(request):
    report_id = request.session.get("last_report_id")
    report = PatientTestReport.objects.get(pk=report_id)
    return render (request, "test_report.html", {
    "report": report,
    "tests": report.tests.all(),
    "total_price": report.total_price
})

# def test_view(request):
#     ob=Laboratory_test.objects.all()
#     return render(request,"labatory_test.html",{"testdata":ob})

def test_view(request):
    email = request.session.get("email")
    logged_in_user = Register_Master.objects.get(Email=email)
    if request.method == "POST":
        selected_ids = request.POST.getlist("selected_tests")
        patient = logged_in_user
        tests = Laboratory_test.objects.filter(test_id__in=selected_ids)
        total_price = sum(test.test_price for test in tests)
        report = PatientTestReport.objects.create(patient=patient, total_price=total_price)
        report.tests.set(tests)
        report.save()
        request.session ["last_report_id"] = report.report_id
        return redirect("test_report")
    ob = Laboratory_test.objects.all()
    return render(request,"labatory_test.html", {"testdata": ob, "user": logged_in_user})


def patient_dashboard(request):
    Appointment=""
    if request.method=="POST":
        pmobile=request.POST["pmobile"]
        if pmobile:
            Appointment=Doctor_Appointment.objects.filter(p_mobile=pmobile)

    return render(request,"patient_dashboard.html",{"msg":Appointment})


def take_appointment(request):
    if request.method=="POST":
        doct_name=request.POST["dname"]
        doct_email=request.POST["demail"]
        demail=Register_Master.objects.get(Email=doct_email)
        doct_mobile=request.POST["dmobile"]
        p_name=request.POST["pname"]
        p_mobile=request.POST["pmobile"]
        p_email=request.POST["pemail"]
        p_dob=request.POST["pdob"]
        p_gender=request.POST["pgender"]
        p_address=request.POST["paddress"]
        p_name=request.POST["pname"]
        diseases=request.POST["diseases"]
        ob=Doctor_Appointment.objects.create(
            doct_name=doct_name,
            doct_contact=doct_mobile,
            doct_email=demail,
            p_name=p_name,
            p_mobile=p_mobile,
            p_address=p_address,
            p_gender=p_gender,
            dob=p_dob,
            p_disease=diseases,
        )
        ob.save()
        return redirect("success")


    return render(request,'book_appointment.html')


def success(request):
    return render(request,"success_page.html")

def phome(request):
    pname=request.session.get('name')
    return render(request,"phome.html",{'Pname':pname})

def doctorview(request):
    ob=Register_Master.objects.filter(Role_name="doctor")
    if request.method=="POST":
        demail=request.POST["email"]
        btn=request.POST["btn"]
        if btn=="Appointment":
            try:
                obj=Register_Master.objects.get(Email=demail)
                pemail=request.session.get('email')
                obj1=Register_Master.objects.get(Email=pemail)
                return render(request,'book_appointment.html',{'Ddata':obj,'pdata':obj1})
            except Register_Master.DoesNotExist:
                return render(request, 'book_appointment.html', {'error': "Doctor or patient not found."})
            except Exception as e:
                return render(request, 'book_appointment.html', {'error': f"An unexpected error occurred: {e}"})


    return render(request,"doctorview.html",{'ddata':ob})