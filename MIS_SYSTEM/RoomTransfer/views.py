from django.shortcuts import render
from Accounts.models import Employee, Department, Form
from RoomTransfer.models import RoomTransfer
from datetime import datetime

    
def RoomTransfer(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Room Transfer choose.html",{'data':data}) 


def RoomTransferPermanent(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Room Transfer - Permanent.html",{'data':data})

def RoomTransferTemporary(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Schedule Transfer - Temporary.html",{'data':data})