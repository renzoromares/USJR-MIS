from django.shortcuts import render
from Accounts.models import Employee, Department, Form
from RoomTransfer.models import RoomTransfer
from datetime import datetime

def RoomTransfer(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    employeeID = Employee.objects.get(Id_Number = id)
    dateApprove = None
    
    if (request.method == "POST"):
        choiceTransfer = request.POST.get('Room')
        if(choiceTransfer == "Permanent"):
            return render(request,"Room Transfer - Permanent.html")

       # if (request.method == "POST"):
           # employeeID = Employee.objects.get(Id_Number = id)
            #form = Form(Id_Number = employeeID, Type = 'RoomTransfer_Permanent' , Date_Requested = datetime.today().strftime('%Y-%m-%d'),Date_Approved = dateApprove ,Status = 'Pending')  
            #form.save()
            #transferPermanent = RoomTransfer(Id_Number = employeeID, Type = 'RoomTransfer_Permanent', Date_Notify = request.POST["Date_Notify"], Subject = request.POST["Subject"], Offer_Code = request.POST["Offer_Code"], Time_Day = request.POST["Time_Day"], Room_From = request.POST["Room_From"], Date_Effective = request.POST["Date_Effective"], Reason = request.POST["Reason"])           
            #transferPermanent.save()
            #return render(request,"Room Transfer choose.html",{'data':data}) 
            #return render(request,"Room Transfer - Permanent.html") 
              
        if(choiceTransfer == "Temporary"):
            return render(request,"Room Transfer - Temporary.html",{'data':data})
            if request.method == 'POST':
                #form = Form(Id_Number = employeeID, Type = 'RoomTransfer_Temporary' , Date_Requested = datetime.today().strftime('%Y-%m-%d'),Date_Approved = dateApprove ,Status = 'Pending')  
                #form.save()
                transferTemporary = RoomTransfer(Id_Number = employeeID, Type = 'RoomTransfer_Permanent',Date_Notify = request.POST["NOTIFY"], Subject = request.POST["Subject"], Offer_Code = request.POST["Offer_Code"], Time_Day = request.POST["Time_Day"], Room_From = request.POST["Room_From"], Date_Effective=request.POST["Date_Effective"], Reason = request.POST["Reason"])
                transferTemporary.save() 
                return render(request,"Room Transfer - Temporary.html") 
                #return render(request,"Room Transfer - Temporary.html") 
    else:
        return render(request,"Room Transfer choose.html",{'data':data}) 
