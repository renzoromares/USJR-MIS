from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department


def Profile(request, id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number= id)
    return render(request,"View Profile.html", {'data' : data}) 




    
    
