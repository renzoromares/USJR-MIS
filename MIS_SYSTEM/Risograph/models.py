from django.db import models
from Accounts.models import Form


class Risograph(models.Model):
    Form_ID = models.ForeignKey(Form,on_delete=models.CASCADE)
    ReqSlipNo = models.CharField(max_length= 100, null=False)
    Date = models.DateField()
    Department = models.CharField(max_length=100,null=False)
    Time_in = models.TimeField()
    Time_out = models.TimeField()
    Paper_Type = models.CharField(max_length=20, null=False )
    No_of_Copies = models.IntegerField(null=False)
    Size = models.CharField(max_length=20, null=False)
    File = models.ImageField(upload_to='pictures')





