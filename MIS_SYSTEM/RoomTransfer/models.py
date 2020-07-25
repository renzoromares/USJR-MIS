from django.db import models
from Accounts.models import Form

class RoomTransfer(models.Model):
    Form_ID = models.ForeignKey(Form,on_delete=models.CASCADE)
    Type = models.CharField(max_length=20,null=False)
    Date_Notify = models.DateField()
    Subject = models.CharField(max_length=30,null=False)
    Offer_Code = models.CharField(max_length=20, null=False)
    Time_Day = models.CharField(max_length=20, null=False)
    Room_From = models.CharField(max_length=20, null=False)
    Date_Effective = models.DateField()
    Reason = models.TextField(max_length=100, null=False    )
