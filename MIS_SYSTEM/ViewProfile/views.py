from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department


def Profile(request, id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number= id)
    if data.Status_Dept == "Faculty":
        status = 1
    elif data.Status_Dept == "Chairman":
        status = 1
    elif data.Status_Dept == "Dean":
        status = 1
    else:
        status = 0
    return render(request,"View Profile.html", {'data' : data, 'status': status}) 




    
    
