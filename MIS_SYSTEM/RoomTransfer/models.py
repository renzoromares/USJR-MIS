from django.db import models
from Accounts.models import Employee

class RoomTransfer(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Type = models.CharField(max_length=20,null=False)
    Date_Notify = models.DateField()
    Subject = models.CharField(max_length=30,null=False)
    Offer_Code = models.CharField(max_length=20, null=False)
    Time_Day = models.CharField(max_length=20, null=False)
    Room_From = models.CharField(max_length=20, null=False)
    #Room_To = models.CharField(max_length=20, null=False)<!--add more column) to be migrated
    Date_Effective = models.DateField()
    Reason = models.TextField(max_length=100, null=False    )

    class Meta:
        db_table = 'RoomTransfer'