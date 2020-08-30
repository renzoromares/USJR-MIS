from django.shortcuts import render, redirect
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from .models import Room_Transfer
from datetime import datetime

   
def RoomTransfer(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)   
    if request.method == "POST":
        if request.POST["RoomTransfer"] =="Permanent":
            return redirect("roomtransferpermanent",id =data.Id_Number.Id_Number)
        
        elif request.POST["RoomTransfer"] =="Temporary":
            return redirect("roomtransfertemporary",id = data.Id_Number.Id_Number)  
    else:        
        return render(request,"Room Transfer choose.html",{'data':data}) 


def RoomTransferPermanent(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type='RoomTransfer(Permanent)',Date_Requested=datetime.today(),Date_Approved=None,Status='Pending')
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        roomTransfer = Room_Transfer(Id_Number=employeeID, Type='RoomTransfer(Permanent)', Date_Notify=datetime.today(), Subject=request.POST["Subject"], Offer_Code=request.POST["Offer_Code"], Time_Day=request.POST["Time_Day"], Room_From=request.POST["Room_From"], Room_To=request.POST["Room_To"],Date_Effective=request.POST["Date_Effective"] ,Reason=request.POST["Reason"], FormID = formPK)
        roomTransfer.save()
        memo_roomTransfer = Memo_Routing(Id_Number=employeeID, Type_Request = 'RoomTransfer(Permanent)', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
        memo_roomTransfer.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'RoomTransfer(Permanent)', Type='Submitted', Date = datetime.today())
        history.save()
        return redirect("transachis", id = data.Id_Number.Id_Number)
    
    else: 
        return render(request,"Room Transfer - Permanent.html",{'data':data})

def RoomTransferTemporary(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    if request.method == "POST":
        form = Form(Id_Number=employeeID, Type='RoomTransfer(Temporary)',Date_Requested=datetime.today(),Date_Approved=None,Status='Pending')
        form.save()
        formPK = Form.objects.get(Form_ID = form.pk)
        roomTransfer = Room_Transfer(Id_Number=employeeID, Type='RoomTransfer(Temporary)', Date_Notify=datetime.today(), Subject=request.POST["Subject"], Offer_Code=request.POST["Offer_Code"], Time_Day=request.POST["Time_Day"], Room_From=request.POST["Room_From"], Room_To=request.POST["Room_To"],Date_Effective=request.POST["Date_Effective"],Reason=request.POST["Reason"], FormID = formPK)
        roomTransfer.save()
        memo_roomTransfer = Memo_Routing(Id_Number=employeeID, Type_Request = 'RoomTransfer(Temporary)', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
        memo_roomTransfer.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'RoomTransfer(Temporary)', Type='Submitted', Date = datetime.today())
        history.save()
        return redirect("transachis", id = data.Id_Number.Id_Number)
    
    else: 
        return render(request,"Room Transfer - Temporary.html",{'data':data})