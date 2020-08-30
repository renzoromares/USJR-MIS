from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Employee, Department, TransacHistory
from django.contrib import messages
from ViewProfile.views import Profile
from ViewRequest.views import ViewRequestFac,ViewRequestPres,ViewRequestReads

def Home(request):
    
    if request.method == "POST":
        if Employee.objects.filter(Id_Number=request.POST["ID_Number"]).exists() and Employee.objects.filter(Password=request.POST["password"]).exists():
            data = Department.objects.prefetch_related('Id_Number').get(Id_Number= request.POST["ID_Number"])
            return render(request, "Dashboard.html", {'data' : data})  
        else:
            return redirect("home")
    else:
        return render(request,'login.html')



def Register(request):
    
    if request.method == "POST":
        if Employee.objects.filter(Id_Number=request.POST["ID"]).exists():
            messages.error(request, "ID Number has been taken by another account")
            return redirect("register")
        
        elif Employee.objects.filter(Email=request.POST["email"]).exists():
            messages.warning(request, "Email has been taken by another account")
            return redirect("register")
        
        elif Employee.objects.filter(Contact=request.POST["contact_number"]).exists():
            messages.error(request, "Contact Number has been taken by another account")
            return redirect("register")    
            
        else:
            signUpEmployee = Employee(Id_Number = request.POST["ID"], First_Name = request.POST["first_name"], Last_Name=request.POST["last_name"], Email = request.POST["email"], Contact = request.POST["contact_number"], Password = request.POST["password"])
            signUpEmployee.save()
            id = Employee.objects.get(Id_Number = request.POST["ID"])
            signUpDepartment = Department(Id_Number=id, department=request.POST["Department"],Status_Dept=request.POST["Status"],College=request.POST["College"])    
            signUpDepartment.save()
            return redirect("home")
    
    else:
        return render(request,"Sign-Up.html")


    
def Dashboard(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Dashboard.html", {'data' : data})


def TransactionHistory(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    datatrans = TransacHistory.objects.filter(Id_Number = id)
    return render(request,"TransactionHistory.html", {'data' : data, 'datatrans' : datatrans})
    