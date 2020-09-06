from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory, TransacHistoryBackUp
from MemoRouting.models import Memo_Routing
from Risograph.models import risograph
from datetime import datetime

def Risograph(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number=id)
    if request.method == "POST":
        upload_file = request.FILES['myfile']        
        form = Form(Id_Number=employeeID, Type="Risograph", Date_Requested=datetime.today(),Date_Approved=None,Status="Pending")
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        _risograph = risograph(Id_Number=employeeID,Date=datetime.today(),Department=request.POST["College/Department"],Paper_Type=request.POST["Paper_Type"], No_of_Copies=request.POST["No_Of_Copies"],Size=request.POST["PaperSize"], FormID = formPK, File = upload_file)
        _risograph.save()
        memo_risograph = Memo_Routing(Id_Number=employeeID, Type_Request = 'Risograph', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
        memo_risograph.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Risograph', Type='Submitted', Date = datetime.today())
        history.save()
        historyback = TransacHistoryBackUp(Id_Number = employeeID, Transac_Type = 'Risograph', Type='Submitted', Date = datetime.today())
        historyback.save()
        return redirect("transachis", id = data.Id_Number.Id_Number) 
    else:
        return render(request,"Risograph.html", {'data' : data}) 
    
