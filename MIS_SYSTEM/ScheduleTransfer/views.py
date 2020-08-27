from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from .models import Schedule_Transfer
from datetime import datetime


def ScheduleTransfer(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)   
    if request.method == "POST":
        if request.POST["transfer"] =="option1":
            return redirect("schedtransferpermanent",id =data.Id_Number.Id_Number)
        
        elif request.POST["transfer"] =="option2":
            return redirect("schedtransfertemporary",id = data.Id_Number.Id_Number)  
    else:        
        return render(request,"ScheduleTransfer.html",{'data':data}) 


def ScheduleTransferPermanent(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type='ScheduleTransfer(Permanent)',Date_Requested=datetime.today().strftime('%Y-%m-%d'),Date_Approved=None,Status='Pending')
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        schedTransfer = Schedule_Transfer(Id_Number=employeeID, Type='ScheduleTransfer(Permanent)', Date_Notify=datetime.today().strftime('%Y-%m-%d'), Subject=request.POST["Subject"], Offer_Code=request.POST["Offer_Code"], Time_Day=request.POST["Time_Day"], Schedule_From=request.POST["Schedule_From"], Schedule_To=request.POST["Schedule_To"],Reason=request.POST["Reason"], FormID = formPK)
        schedTransfer.save()
        memo_schedTransfer = Memo_Routing(Id_Number=employeeID, Type_Request = 'ScheduleTransfer(Permanent)', Date_Faculty_Submitted = datetime.today().strftime('%Y-%m-%d'), FormID = formPK)
        memo_schedTransfer.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'ScheduleTransfer(Permanent)', Type='Submitted', Date = datetime.today().strftime('%Y-%m-%d'))
        history.save()
        return render(request,"Schedule Transfer - Permanent.html",{'data':data})
    
    else: 
        return render(request,"Schedule Transfer - Permanent.html",{'data':data})

def ScheduleTransferTemporary(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type='ScheduleTransfer(Temporary)',Date_Requested=datetime.today().strftime('%Y-%m-%d'),Date_Approved=None,Status='Pending')
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        schedTransfer = Schedule_Transfer(Id_Number=employeeID, Type='ScheduleTransfer(Temporary)', Date_Notify=datetime.today().strftime('%Y-%m-%d'), Subject=request.POST["Subject"], Offer_Code=request.POST["Offer_Code"], Time_Day=request.POST["Time_Day"], Schedule_From=request.POST["Schedule_From"], Schedule_To=request.POST["Schedule_To"],Reason=request.POST["Reason"], FormID = formPK)
        schedTransfer.save()
        memo_schedTransfer = Memo_Routing(Id_Number=employeeID, Type_Request = 'ScheduleTransfer(Temporary)', Date_Faculty_Submitted = datetime.today().strftime('%Y-%m-%d'), FormID = formPK)
        memo_schedTransfer.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'ScheduleTransfer(Temporary)', Type='Submitted', Date = datetime.today().strftime('%Y-%m-%d'))
        history.save()
        return render(request,"Schedule Transfer - Temporary.html",{'data':data})
    
    else: 
        return render(request,"Schedule Transfer - Temporary.html",{'data':data})    
