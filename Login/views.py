from django.shortcuts import render, redirect
from REGISTER.models import Register_Master

def login(request):
    if request.method == "POST":
        Email = request.POST["email"]
        Pwd = request.POST["pwd"]

        try:
            ob = Register_Master.objects.get(Email=Email, Password=Pwd)

            request.session['name'] = ob.Name
            request.session['email'] = ob.Email

            if ob.Role_name == "doctor":
                return redirect("dhome")
            elif ob.Role_name == "patient":
                return redirect("phome")
            elif ob.Role_name == "staff":
                return redirect("shome")
            elif ob.Role_name == "ehrs_admin":
                return redirect("ahome")
            else:
                return render(request, "login.html", {"msg": "Invalid role"})

        except Register_Master.DoesNotExist:
            return render(request, "login.html", {"msg": "Invalid username or password"})
        except Exception as e:
            return render(request, "login.html", {"msg": "Error: " + str(e)})

    return render(request, "login.html")
