from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from .models import Certifacate
from datetime import datetime

def RequestCertificate(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type='Request for Certificate',Date_Requested=datetime.today().strftime('%Y-%m-%d'),Date_Approved=None, Status='Pending')
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        certificate = Certifacate(Id_Number=employeeID,Certificate_To_Request=request.POST["Certificate"],Others_Certificate=request.POST["Others_Certificate"],Reason=request.POST["Reason"], FormID = formPK)
        certificate.save()
        memo_certificate = Memo_Routing(Id_Number = employeeID, Type_Request = 'Request for Certificate', Date_Faculty_Submitted = datetime.today().strftime('%Y-%m-%d,%H:%M'), FormID = formPK)
        memo_certificate.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Certificate', Type='Submitted', Date = datetime.today().strftime('%Y-%m-%d,%H:%M'))
        history.save()
        return render(request,"Request Certificate.html", {'data' : data}) 
            
    else:
        return render(request,"Request Certificate.html", {'data' : data}) 