from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from FileLeave.models import Leave
from datetime import datetime


def FileLeave(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number= id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None
    
    if request.method == 'POST':
        form = Form(Id_Number = employeeID, Type = 'File Leave' , Date_Requested = datetime.today().strftime('%Y-%m-%d'),Date_Approved = dateApprove ,Status = 'Pending')  
        form.save()
        tempStatus = request.POST.get('status')
        tempLeave = request.POST.get('typeofLeave')
        upload_file = request.FILES['document']

        fileleave = Leave(Id_Number = employeeID, Employee_Status = tempStatus ,Typeof_Leave = tempLeave , Date_Start = request.POST["Date_Start"],Date_End = request.POST["Date_End"],Period_Days ='3',Reason = request.POST["Reasons"],Image = upload_file)
        fileleave.save()
        memo_fileleave = Memo_Routing(Id_Number = employeeID, Type_Request = 'File Leave', Date_Faculty_Submitted = datetime.today().strftime('%Y-%m-%d'))
        memo_fileleave.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'File Leave', Type='Submitted', Date = datetime.today().strftime('%Y-%m-%d'))
        history.save()
        return render(request,"File a Leave.html", {'data' : data}) 
    else:
        return render(request,"File a Leave.html", {'data' : data}) 

