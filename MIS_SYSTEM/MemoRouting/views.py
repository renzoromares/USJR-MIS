from django.shortcuts import render,redirect
from Accounts.models import Employee, Department


def MemoRouting(request,id):
    data = Department.objects.prefetch_related('Id_Number').get(Id_Number = id)
    return render(request,"Memo Routing.html", {'data' : data}) 
    


    
    
