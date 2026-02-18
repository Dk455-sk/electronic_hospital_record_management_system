from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from REGISTER.models import Register_Master
from .forms import testForm
from .models import Bill
from Patient.models import *
from django.contrib.auth import logout

# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('home')

def applytest(request):
    ob=PatientTestReport.objects.all()
    return render(request,"applytest.html",{'rdata':ob})


def add_test(request):
    formobj=testForm()
    if request.method=="POST":
        formobj=testForm(request.POST)
        if formobj.is_valid():
            formobj.save()
    return render(request,'add_test.html',{'form':formobj})

def patient_doctor_view(request):
    ob=Register_Master.objects.filter(Role_name="patient")
    ob1=Register_Master.objects.filter(Role_name="doctor")

    return render(request,"pdviewdata.html",{'pdata':ob,"Ddata":ob1})


def shome(request):
    sname=request.session.get('name')
    
    return render(request,"shome.html",{'Sname':sname})


def generate_bill(request):
    patients = Register_Master.objects.filter(Role_name='patient')
    ob = None
    selected_id = None

    if request.method == "POST":
        patient_id = request.POST.get("patient_id")
        selected_id = patient_id

        try:
            ob = Register_Master.objects.get(Reg_id=patient_id, Role_name='patient')
        except Register_Master.DoesNotExist:
            ob = None

        consultation = float(request.POST.get("consultation", 0))
        lab_tests = float(request.POST.get("lab_tests", 0))
        medication = float(request.POST.get("medication", 0))
        room = float(request.POST.get("room", 0))
        tax = float(request.POST.get("tax", 0))

        subtotal = consultation + lab_tests + medication + room
        tax_amount = subtotal * (tax / 100)
        total = subtotal + tax_amount

        # Save bill to database
        bill = Bill.objects.create(
            patient=ob,
            consultation=consultation,
            lab_tests=lab_tests,
            medication=medication,
            room=room,
            tax=tax,
            subtotal=subtotal,
            tax_amount=tax_amount,
            total=total
        )

        # Render success page with saved bill
        return render(request, "bill_success.html", {
            "bill": bill,
            "patient_name": ob.Name if ob else "Unknown"
        })

    return render(request, "billing.html", {
        "patients": patients,
        "patient_name": ob.Name if ob else None,
        "selected_id": selected_id,
    })



def bill_records(request):
    query = request.GET.get("q")
    if query:
        bills = Bill.objects.filter(patient__Reg_id__icontains=query)
    else:
        bills = Bill.objects.all()
    return render(request, "billing_record.html", {"bills": bills, "query": query})

def cancel_bill(request, bill_id):
    bill = get_object_or_404(Bill, id=bill_id)
    bill.delete()
    return redirect('bill_records')


