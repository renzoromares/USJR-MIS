from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department
# Create your views here.

def ViewRequestPres(request):
    return render(request,"ViewRequestPres.html") 

def ViewRequestReads(request):
    return render(request,"ViewRequestReads.html") 

def ViewRequestFac(request):
    return render(request,"ViewRequestsFac.html") 