from django.db import models
from Accounts.models import Employee

class Risograph(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    ReqSlipNo = models.CharField(max_length= 100, null=False)
    Date = models.DateField()
    Department = models.CharField(max_length=100,null=False)
    Time_in = models.TimeField()
    Time_out = models.TimeField()
    Paper_Type = models.CharField(max_length=20, null=False )
    No_of_Copies = models.IntegerField(null=False)
    Size = models.CharField(max_length=20, null=False)
    File = models.ImageField(upload_to='pictures')

    class Meta:
        db_table = 'Risograph'




