from django.db import models
from Accounts.models import Employee

class Makeup_Class(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Reason = models.TextField(max_length=100, null=False)
    Subject = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.CharField(max_length=20, null=False)
    Romm = models.CharField(max_length=20, null=False)
    Date_Of= models.DateField()

    
    class Meta:
        db_table = 'Makeup_Class'