from django.shortcuts import render,redirect
from Accounts.models import Employee, Department, Form, TransacHistory
from MemoRouting.models import Memo_Routing
from datetime import datetime
from CashAdvance.models import Cash_Advance


def CashAdvance(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number= id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None
    if(request.method == "POST"):    
        form = Form(Id_Number = employeeID, Type = 'Cash Advance' , Date_Requested = datetime.today(),Date_Approved = dateApprove ,Status = 'Pending')  
        form.save()
        print(form.pk)
        formPK = Form.objects.get(Form_ID = form.pk)
        cash_advance = Cash_Advance(Id_Number = employeeID, Cash_Amount = request.POST["Amount"], Reason  = request.POST["Reason"], FormID = formPK)
        cash_advance.save()
        memo_cash_advance = Memo_Routing(Id_Number = employeeID, Type_Request = 'Cash Advance', Date_Faculty_Submitted = datetime.today(), FormID = formPK, Status = 'Pending')
        memo_cash_advance.save()
        history = TransacHistory(Id_Number = employeeID, Transac_Type = 'Cash Advance', Type='Submitted', Date = datetime.today())
        history.save()
        return redirect("transachis", id = data.Id_Number.Id_Number)
    else:     
        return render(request,"Cash Advance.html", {'data' : data}) 
