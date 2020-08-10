from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form
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

        fileleave = Leave(Id_Number = employeeID, Designation  = request.POST["Designation"], Employee_Status = tempStatus ,Typeof_Leave = tempLeave , Date_Start = request.POST["Date_Start"],Date_End = request.POST["Date_End"],Period_Days ='3',Reason = request.POST["Reasons"],Image = upload_file)
        fileleave.save()
        return render(request,"File a Leave.html", {'data' : data}) 
    else:
        return render(request,"File a Leave.html", {'data' : data}) 

