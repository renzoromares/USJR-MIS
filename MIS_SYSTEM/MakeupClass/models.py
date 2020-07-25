from django.db import models
from Accounts.models import Form

class Makeup_Class(models.Model):
    Form_ID = models.ForeignKey(Form,on_delete=models.CASCADE)
    Reason = models.TextField(max_length=100, null=False)
    Subject = models.CharField(max_length=20)
    Date = models.DateField()
    Time = models.CharField(max_length=20, null=False)
    Romm = models.CharField(max_length=20, null=False)
    Date_Of= models.DateField()