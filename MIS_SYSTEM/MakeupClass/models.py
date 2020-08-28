from django.db import models
from Accounts.models import Employee, Form

class Makeup_Class(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    College = models.CharField(max_length=20, null=False)
    Reason = models.TextField(max_length=100, null=False)
    OfferCode = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.CharField(max_length=20, null=False)
    Room = models.CharField(max_length=20, null=False)
    Date_Of= models.DateField()
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)

    
    class Meta:
        db_table = 'Makeup_Class'