from django.shortcuts import render, redirect
from django.http import HttpResponse
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from Risograph.models import risograph
from CashAdvance.models import Cash_Advance
from FileLeave.models import Leave
from MakeupClass.models import Makeup_Class
from RequestCertificate.models import Certifacate
from RoomTransfer.models import Room_Transfer
from ScheduleTransfer.models import Schedule_Transfer
from datetime import datetime
from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
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
        dataForm = Employee.objects.filter(department__Status_Dept = 'Faculty', department__department = data.department, form__Status = 'Pending', memo_routing__Date_Chairman_Approved = None, memo_routing__FormID__isnull = False).distinct('memo_routing__FormID').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
    elif data.Status_Dept=='Faculty':
        dataForm = Employee.objects.filter(Id_Number = id, form__Form_ID__isnull = False).values('form__Type','form__Date_Requested','form__Date_Approved','form__Status')
    elif data.Status_Dept=='Dean':
        dataForm = Employee.objects.filter(department__Status_Dept__in = ('Faculty','Chairman'),department__College = data.College, memo_routing__Date_Dean_Approved = None, memo_routing__Date_Chairman_Approved__isnull = False, form__Form_ID__isnull = False, form__Status = 'Pending').distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
    elif data.Status_Dept=='VP Academics':
        dataForm = Employee.objects.filter(memo_routing__Date_Chairman_Approved__isnull = False, memo_routing__Date_Dean_Approved__isnull = False, memo_routing__Date_VP_Acad_Approved = None, form__Form_ID__isnull = False, form__Status = 'Pending', memo_routing__Type_Request__in = ('File Leave','Make-up Class','Request for Certificate','RoomTransfer(Permanent)','RoomTransfer(Temporary)','ScheduleTransfer(Temporary)','ScheduleTransfer(Permanent)','Cash Advance')).distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
    elif data.Status_Dept=='President':
        dataForm = Employee.objects.filter(memo_routing__Date_Chairman_Approved__isnull = False, memo_routing__Date_Dean_Approved__isnull = False, memo_routing__Date_VP_Acad_Approved__isnull = False, memo_routing__Date_President_Approved = None, form__Form_ID__isnull = False, memo_routing__Type_Request__in = ('Cash Advance','File Leave'), form__Status = 'Pending').distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
    elif data.Status_Dept=='HR':
        dataForm = Employee.objects.filter(memo_routing__Date_Chairman_Approved__isnull = False, memo_routing__Date_Dean_Approved__isnull = False, memo_routing__Date_VP_Acad_Approved__isnull = False, memo_routing__Date_President_Approved__isnull = False, memo_routing__Date_HR_Approved = None, form__Form_ID__isnull = False, form__Status = 'Pending', memo_routing__Type_Request__in = ('Cash Advance','File Leave')).distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
    elif data.Status_Dept=='PAO':
        dataForm = Employee.objects.filter(memo_routing__Date_Chairman_Approved__isnull = False, memo_routing__Date_Dean_Approved__isnull = False, memo_routing__Date_PAO_Approved = None, form__Form_ID__isnull = False, form__Status = 'Pending', memo_routing__Type_Request = 'Risograph').distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
    elif data.Status_Dept=='Accounting':
        dataForm = Employee.objects.filter(memo_routing__Date_Chairman_Approved__isnull = False, memo_routing__Date_Dean_Approved__isnull = False, memo_routing__Date_VP_Acad_Approved__isnull = False, memo_routing__Date_President_Approved__isnull = False, memo_routing__Date_HR_Approved__isnull = False, memo_routing__Date_Accounting_Approved = None, form__Form_ID__isnull = False, form__Status = 'Pending', memo_routing__Type_Request = 'Cash Advance').distinct('memo_routing__id').values('memo_routing__id','First_Name','Last_Name','memo_routing__Type_Request','memo_routing__Date_Faculty_Submitted','memo_routing__FormID')
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
    
def ViewRequestDetails(request,id,idf,idm):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    dataMemo = Memo_Routing.objects.get(id = idm)
    
    if dataMemo.Type_Request == 'Cash Advance':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = Cash_Advance.objects.get(FormID = idf)
    elif dataMemo.Type_Request == 'File Leave':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = Leave.objects.get(FormID = idf)
    elif dataMemo.Type_Request == 'Make-up Class':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = Makeup_Class.objects.get(FormID = idf)
    elif dataMemo.Type_Request == 'Risograph':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = risograph.objects.get(FormID = idf)
    elif dataMemo.Type_Request == 'Request for Certificate':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = Certifacate.objects.get(FormID = idf)
    elif dataMemo.Type_Request == 'RoomTransfer(Permanent)' or dataMemo.Type_Request == 'RoomTransfer(Temporary)':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = Room_Transfer.objects.get(FormID = idf)
    elif dataMemo.Type_Request == 'ScheduleTransfer(Permanent)' or dataMemo.Type_Request == 'ScheduleTransfer(Temporary)':
        dataEm = Department.objects.prefetch_related('Id_Number').get(Id_Number = dataMemo.Id_Number)
        dataDetails = Schedule_Transfer.objects.get(FormID = idf)
    if request.method == "POST":
        if request.POST.get('Memo_ID') == idm:
            updateMemo = Memo_Routing.objects.get(id = request.POST["Memo_ID"])
            if data.Status_Dept == 'Chairman':              
                updateMemo.Date_Chairman_Approved=datetime.today().strftime('%Y-%m-%d')
                updateMemo.save(update_fields=['Date_Chairman_Approved'])
                history = TransacHistory(Id_Number = data.Id_Number, Transac_Type = dataDetails.FormID.Type, Type='Approved', Date = datetime.today())
                history.save() 
            elif data.Status_Dept == 'Dean':
                updateMemo.Date_Dean_Approved=datetime.today().strftime('%Y-%m-%d')
                updateMemo.save(update_fields=['Date_Dean_Approved'])
                history = TransacHistory(Id_Number = data.Id_Number, Transac_Type = dataDetails.FormID.Type, Type='Approved', Date = datetime.today())
                history.save() 
            elif data.Status_Dept == 'VP Academics':
                updateMemo.Date_VP_Acad_Approved=datetime.today().strftime('%Y-%m-%d')
                updateMemo.save(update_fields=['Date_VP_Acad_Approved'])
                history = TransacHistory(Id_Number = data.Id_Number, Transac_Type = dataDetails.FormID.Type, Type='Approved', Date = datetime.today())
                history.save() 
            elif data.Status_Dept == 'President':
                updateMemo.Date_President_Approved=datetime.today().strftime('%Y-%m-%d')
                updateMemo.save(update_fields=['Date_President_Approved'])
                history = TransacHistory(Id_Number = data.Id_Number, Transac_Type = dataDetails.FormID.Type, Type='Approved', Date = datetime.today())
                history.save() 
            elif data.Status_Dept == 'HR':
                updateMemo.Date_HR_Approved=datetime.today().strftime('%Y-%m-%d')
                updateMemo.save(update_fields=['Date_HR_Approved'])
                history = TransacHistory(Id_Number = data.Id_Number, Transac_Type = dataDetails.FormID.Type, Type='Approved', Date = datetime.today())
                history.save() 
            elif data.Status_Dept == 'Accounting':
                updateMemo.Date_Accounting_Approved=datetime.today().strftime('%Y-%m-%d')
                updateMemo.save(update_fields=['Date_Accounting_Approved'])
                history = TransacHistory(Id_Number = data.Id_Number, Transac_Type = dataDetails.FormID.Type, Type='Approved', Date = datetime.today())
                history.save() 
            return redirect("viewrequestfac", id =data.Id_Number.Id_Number)            
        elif request.POST.get('Form_ID') == idf:
            updateForm = Form.objects.get(Form_ID = request.POST["Form_ID"])
            updateForm.Status = 'Declined'
            updateForm.save(update_fields=['Status'])
            return redirect("viewrequestfac", id =data.Id_Number.Id_Number)
        #updateForm = Form.objects.get(id = request.POST["Form_ID"])
        #if data.Status_Dept == 'Chairman':

    return render(request,"ViewRequestDetails.html",{'data' : data, 'dataDetails' : dataDetails, 'dataEm' : dataEm, 'dataMemo' : dataMemo})

