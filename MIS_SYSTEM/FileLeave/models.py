from django.db import models
from Accounts.models import Form

class Leave(models.Model):
    Form_ID = models.ForeignKey(Form,on_delete = models.CASCADE)
    Designation = models.CharField(max_length=100, null=False)
    Employee_Status = models.CharField(max_length=20, null=False)
    Date_Start = models.DateField()
    Date_End =  models.DateField()
    Period_Days = models.IntegerField()
    Reason = models.TextField(max_length=100,null=False)
