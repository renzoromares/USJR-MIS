from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from Risograph.models import risograph
from datetime import datetime

def Risograph(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number=id)
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type="Risograph", Date_Requested=datetime.today().strftime('%Y-%m-%d'),Date_Approved=None,Status="Pending")
        form.save()
        _risograph = risograph(Id_Number=employeeID,Date=datetime.today().strftime('%Y-%m-%d'),Department=request.POST["College/Department"],Paper_Type=request.POST["Paper_Type"], No_of_Copies=request.POST["No_Of_Copies"],Size=request.POST["PaperSize"])
        _risograph.save()
        memo_risograph = Memo_Routing(Id_Number=employeeID, Type_Request = 'Risograph', Date_Faculty_Submitted = datetime.today().strftime('%Y-%m-%d'))
        memo_risograph.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Risograph', Type='Submitted', Date = datetime.today().strftime('%Y-%m-%d'))
        history.save()
        return render(request,"Risograph.html", {'data' : data}) 
    else:
        return render(request,"Risograph.html", {'data' : data}) 
    
