from django.shortcuts import render,redirect
from Accounts.models import Employee, Department

def RequestCertificate(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Request Certificate.html", {'data' : data}) 