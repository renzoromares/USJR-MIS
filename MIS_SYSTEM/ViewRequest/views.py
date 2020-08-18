from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department, Form
from MemoRouting.models import Memo_Routing
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
        dataForm = Employee.objects.filter(department__department = data.department, memo_routing__Date_Chairman_Approved = None, form__Form_ID__isnull = False).distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted')
    elif data.Status_Dept=='Faculty':
        dataForm = Employee.objects.filter(Id_Number = id, form__Form_ID__isnull = False).values('form__Type','form__Date_Requested','form__Date_Approved','form__Status')
    elif data.Status_Dept=='Dean':
        dataForm = Employee.objects.filter(department__College = data.College, memo_routing__Date_Dean_Approved = None, memo_routing__Date_Chairman_Approved__isnull = False, form__Form_ID__isnull = False).distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted')
    elif data.Status_Dept=='VP Academics':
        dataForm = Employee.objects.filter(memo_routing__Date_Chairman_Approved__isnull = False, memo_routing__Date_Dean_Approved__isnull = False, memo_routing__Date_VP_Acad_Approved = None, form__Form_ID__isnull = False).distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted')
    if request.method == "POST":
        update=Memo_Routing.objects.get(id = request.POST["Memo_ID"])
        if data.Status_Dept=='Chairman':
            update.Date_Chairman_Approved = datetime.today().strftime('%Y-%m-%d')
            update.save(update_fields=['Date_Chairman_Approved'])
        elif data.Status_Dept=='Dean':
            update.Date_Dean_Approved = datetime.today().strftime('%Y-%m-%d')
            update.save(update_fields=['Date_Dean_Approved'])
        elif data.Status_Dept=='VP Academics':
            update.Date_VP_Acad_Approved = datetime.today().strftime('%Y-%m-%d')
            update.save(update_fields=['Date_VP_Acad_Approved'])
        

    return render(request,"ViewRequestsFac.html", {'data' : data, 'dataForm' : dataForm})

def ViewRequestPao(request,id):
    dataEmployee = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    data = Employee.objects.filter(form__Type='Risograph',form__Status='Pending',risograph__Price = None).distinct('risograph__Risograph_ID').values('risograph__Risograph_ID','risograph__Department','risograph__Paper_Type','risograph__No_of_Copies','risograph__Size','risograph__File','form__Status','form__Date_Approved','form__Date_Requested','form__Form_ID')
    if request.method == "POST": 
        updateRiso=risograph.objects.get(Risograph_ID=request.POST["Riso_ID"])
        updateRiso.Price= request.POST["price"]
        updateRiso.save(update_fields=['Price'])
            
        update=Memo_Routing.objects.get(Form_ID=request.POST["FormID"])
        update.Date_Approved=datetime.today().strftime('%Y-%m-%d')
        update.save(update_fields=['Date_Approved'])
    return render(request,"ViewRequestPAO.html", {'data' : data, 'dataEmployee': dataEmployee}) 


def ViewRequestIMS(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    dataForm = Employee.objects.filter(form__Status='Approved', form__Type__in=('File Leave','Make-up Class','Request for Certificate','RoomTransfer(Permanent)','RoomTransfer(Temporary)','ScheduleTransfer(Temporary)','ScheduleTransfer(Permanent)')).values('First_Name','Last_Name','form__Type','form__Date_Requested','form__Date_Approved','form__Status')
    return render(request,"ViewRequestIMS.html", {'data' : data, 'dataForm' : dataForm})

