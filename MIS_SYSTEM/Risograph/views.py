from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form
from Risograph.models import risograph
from datetime import datetime

def Risograph(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number=id)
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type="Risograph", Date_Requested=datetime.today().strftime('%Y-%m-%d'),Date_Approved=None,Status="Pending")
        form.save()
        _risograph = risograph(Id_Number=employeeID,Date=request.POST["date"],Department=request.POST["College/Department"],Time_in=request.POST["Time_In"],Time_out=request.POST["Time_Out"],Paper_Type=request.POST["Paper_Type"], No_of_Copies=request.POST["No_Of_Copies"],Size=request.POST["PaperSize"],Acetate=request.POST["Acetate"])
        _risograph.save()
        return render(request,"Risograph.html", {'data' : data}) 
    else:
        return render(request,"Risograph.html", {'data' : data}) 
    
