from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department
# Create your views here.


def ViewRequestPres(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"ViewRequestPres.html", {'data' : data}) 

def ViewRequestReads(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"ViewRequestReads.html", {'data' : data}) 

def ViewRequestFac(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"ViewRequestsFac.html", {'data' : data}) 


