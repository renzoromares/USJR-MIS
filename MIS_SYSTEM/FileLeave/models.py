from django.db import models
from Accounts.models import Employee,Form

class Leave(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Employee_Status = models.CharField(max_length=20, null=False)
    Designation = models.CharField(max_length=100, null=False)
    Typeof_Leave = models.CharField(max_length = 30, null = False)
    Date_Start = models.DateField()
    Date_End =  models.DateField()
    Period_Days = models.IntegerField()
    Reason = models.TextField(max_length=100,null=False)
    Image = models.ImageField(null = True, blank = True, upload_to = "images/")
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)
    timeSubmitted = models.TimeField(auto_now=True)
    

    class Meta:
        db_table = 'Leave'
        