from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form
from datetime import datetime
from CashAdvance.models import Cash_Advance


def CashAdvance(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number= id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None
    
    if(request.method == "POST"):
        form = Form(Id_Number = employeeID, Type = 'cashadvance' , Date_Requested = datetime.today().strftime('%Y-%m-%d'),Date_Approved = dateApprove ,Status = 'Pending')  
        form.save()
        cash_advance = Cash_Advance(Id_Number = employeeID, Cash_Amount = request.POST["Amount"], Reason  = request.POST["Reason"] )
        cash_advance.save()
        return render(request,"Cash Advance.html", {'data' : data})
    else:     
        return render(request,"Cash Advance.html", {'data' : data}) 
