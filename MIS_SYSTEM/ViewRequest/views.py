from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department, Form
from Risograph.models import risograph
from datetime import datetime
# Create your views here.


def ViewRequestPres(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"ViewRequestPres.html", {'data' : data}) 

def ViewRequestReads(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"ViewRequestReads.html", {'data' : data}) 

def ViewRequestFac(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    if data.Status_Dept=='Chairman':
        dataForm = Employee.objects.filter(department__department = data.department, form__Status = 'Pending').values('form__Form_ID','First_Name','Last_Name','form__Type','form__Date_Requested','form__Date_Approved','form__Status')
    elif data.Status_Dept=='Faculty':
        dataForm = Employee.objects.filter(Id_Number = id).values('form__Type','form__Date_Requested','form__Date_Approved','form__Status')
    if request.method == "POST":
        formpk=request.POST["Form_ID"]
        update=Form.objects.get(Form_ID = formpk)
        update.Date_Approved=datetime.today().strftime('%Y-%m-%d')
        update.Status='Approved'
        update.save(update_fields=['Date_Approved', 'Status'])

    return render(request,"ViewRequestsFac.html", {'data' : data, 'dataForm' : dataForm})

def ViewRequestPao(request,id):
    data = Employee.objects.filter(form__Type='Risograph',form__Status='Pending',risograph__Price = None).values('risograph__Risograph_ID','risograph__Department','risograph__Paper_Type','risograph__No_of_Copies','risograph__Size','risograph__File','form__Status','form__Date_Approved','form__Date_Requested','form__Form_ID')
    num1= data.count()/2
    if request.method == "POST": 
        updateRiso=risograph.objects.get(Risograph_ID=request.POST["Riso_ID"])
        updateRiso.Price= request.POST["price"]
        updateRiso.save(update_fields=['Price'])
            
        update=Form.objects.get(Form_ID=request.POST["FormID"])
        update.Date_Approved=datetime.today().strftime('%Y-%m-%d')
        update.Status='Approved'
        update.save(update_fields=['Date_Approved', 'Status'])
    return render(request,"ViewRequestPAO.html", {'data' : data, 'num1': num1}) 


def ViewRequestIMS(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    dataForm = Employee.objects.exclude(form__Status = 'Pending', form__Type='Risograph').values('First_Name','Last_Name','form__Type','form__Date_Requested','form__Date_Approved','form__Status')
    return render(request,"ViewRequestsFac.html", {'data' : data, 'dataForm' : dataForm})

