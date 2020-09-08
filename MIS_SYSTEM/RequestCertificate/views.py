from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory, TransacHistoryBackUp
from MemoRouting.models import Memo_Routing
from .models import Certifacate
from datetime import datetime

def RequestCertificate(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type='Request for Certificate',Date_Requested=datetime.today(),Date_Approved=None, Status='Pending')
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        certificate = Certifacate(Id_Number=employeeID,Certificate_To_Request=request.POST["Certificate"],Others_Certificate=request.POST["Others_Certificate"],Reason=request.POST["Reason"], FormID = formPK)
        certificate.save()
        if (data.Status_Dept == "Faculty"):
            memo_certificate = Memo_Routing(Id_Number = employeeID, Type_Request = 'Certificate', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
        if (data.Status_Dept == "Chairman"):
            memo_certificate = Memo_Routing(Id_Number = employeeID, Type_Request = 'Certificate', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today())
        if (data.Status_Dept == "Dean"):
            memo_certificate = Memo_Routing(Id_Number = employeeID, Type_Request = 'Certificate', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today(),Date_Dean_Approved=datetime.today())
        memo_certificate.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Certificate', Type='Submitted', Date = datetime.today())
        history.save()
        historyback = TransacHistoryBackUp(Id_Number = employeeID, Transac_Type = 'Certificate', Type='Submitted', Date = datetime.today())
        historyback.save()
        return redirect("transachis", id = data.Id_Number.Id_Number) 
            
    else:
        return render(request,"Request Certificate.html", {'data' : data}) 