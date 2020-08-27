from django.db import models
from Accounts.models import Employee,Form

class Room_Transfer(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Type = models.CharField(max_length=50,null=False)
    Date_Notify = models.DateField()
    Subject = models.CharField(max_length=50,null=False)
    Offer_Code = models.CharField(max_length=50, null=False)
    Time_Day = models.CharField(max_length=50, null=False)
    Room_From = models.CharField(max_length=50, null=False)
    Room_To = models.CharField(max_length=50, null=False)
    Date_Effective = models.DateField(null=True)
    Reason = models.TextField(max_length=150, null=False)
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)
    timeSubmitted = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'RoomTransfer'