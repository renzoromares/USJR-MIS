from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form
from MakeupClass.models import Makeup_Class
from datetime import datetime

def MakeupClass(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None

    if request.method == 'POST':
        form = Form(Id_Number = employeeID, Type = 'Make-up Class' , Date_Requested = datetime.today().strftime('%Y-%m-%d'),Date_Approved = dateApprove ,Status = 'Pending')  
        form.save()
        if(request.POST.get('options') == "others"):
            makeupclass = Makeup_Class(Id_Number = employeeID  ,College = request.POST["college"],Reason = request.POST["Reason"],OfferCode =request.POST["offercode"] ,Date =  datetime.today().strftime('%Y-%m-%d') ,Time = request.POST["time"], Room= request.POST["room"], Date_Of = request.POST["dateOf"])
            makeupclass.save()
            return render(request,"makeup-class.html", {'data' : data}) 
        else:
            makeupclass = Makeup_Class(Id_Number = employeeID  ,College =  request.POST["college"],Reason = request.POST.get('options'),OfferCode = request.POST["offercode"] ,Date =  datetime.today().strftime('%Y-%m-%d'),Time = request.POST["time"], Room= request.POST["room"], Date_Of = request.POST["dateOf"])
            makeupclass.save()
            return render(request,"makeup-class.html", {'data' : data}) 
    else:
        return render(request,"makeup-class.html", {'data' : data}) 
        