from django.shortcuts import render,redirect
from Accounts.models import Employee, Department
from MemoRouting.models import Memo_Routing


def MemoRouting(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    if request.method == "POST":
        if request.POST["Memo"] == "Outgoing":
            return redirect("memoroutingoutgoing",id =data.Id_Number.Id_Number)
            
        elif request.POST["Memo"] == "Incoming":
            return redirect("memoroutingincoming",id =data.Id_Number.Id_Number)     
    else:
        return render(request,"Memo Routing.html", {'data' : data}) 



def MemoRoutingOutgoing(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Memo Routing.html", {'data' : data}) 


def MemoRoutingIngoing(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    dataMemo = Memo_Routing.objects.filter(Id_Number = id).order_by('Date_Faculty_Submitted')
    return render(request,"Memo Routing - Incoming.html", {'data' : data, 'dataMemo': dataMemo}) 
    
   
    
