from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory, TransacHistoryBackUp
from MemoRouting.models import Memo_Routing
from FileLeave.models import Leave
from datetime import datetime


def FileLeave(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number= id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None
    
    if request.method == 'POST':
        form = Form(Id_Number = employeeID, Type = 'File Leave' , Date_Requested = datetime.today(),Date_Approved = dateApprove ,Status = 'Pending')  
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        tempStatus = request.POST.get('status')
        tempLeave = request.POST.get('typeofLeave')
        upload_file = request.FILES['document']

        fileleave = Leave(Id_Number = employeeID, Employee_Status = tempStatus ,Typeof_Leave = tempLeave , Date_Start = request.POST["Date_Start"],Date_End = request.POST["Date_End"],Period_Days ='3',Reason = request.POST["Reasons"],Image = upload_file, FormID = formPK)
        fileleave.save()
        if (data.Status_Dept == "Faculty"):
            memo_fileleave = Memo_Routing(Id_Number = employeeID, Type_Request = 'File Leave', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
        if (data.Status_Dept == "Chairman"):
            memo_fileleave = Memo_Routing(Id_Number = employeeID, Type_Request = 'File Leave', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today())
        if (data.Status_Dept == "Dean"):
            memo_fileleave = Memo_Routing(Id_Number = employeeID, Type_Request = 'File Leave', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending',Date_Chairman_Approved=datetime.today(),Date_Dean_Approved=datetime.today())
        memo_fileleave.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'File Leave', Type='Submitted', Date = datetime.today())
        history.save()
        historyback = TransacHistoryBackUp(Id_Number = employeeID, Transac_Type = 'File Leave', Type='Submitted', Date = datetime.today())
        historyback.save()
        return redirect("transachis", id = data.Id_Number.Id_Number) 
    else:
        return render(request,"File a Leave.html", {'data' : data}) 

