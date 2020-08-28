from django.db import models
from Accounts.models import Employee,Form

class Schedule_Transfer(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Type = models.CharField(max_length=30,null=False)
    Date_Notify = models.DateField()
    Subject = models.CharField(max_length=100,null=False)
    Offer_Code = models.CharField(max_length=20, null=False)
    Time_Day = models.CharField(max_length=50,null=False)
    Schedule_From = models.CharField(max_length=50,null=False)
    Schedule_To = models.CharField(max_length=50,null=False) 
    Reason = models.TextField(max_length=100, null=False)
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)

    class Meta:
        db_table = 'Schedule_Transfer'