from django.db import models
from Accounts.models import Employee, Form

class risograph(models.Model):
    Risograph_ID = models.AutoField(primary_key=True)
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Date = models.DateField()
    Department = models.CharField(max_length=100,null=False)
    Paper_Type = models.CharField(max_length=50, null=False )
    No_of_Copies = models.IntegerField(null=False)
    Size = models.CharField(max_length=50, null=False)
    File = models.ImageField(upload_to='pictures',null=True)
    Price = models.BigIntegerField(null=True)
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)
    timeSubmitted = models.TimeField(auto_now=True)

    class Meta:
        db_table = 'Risograph'




