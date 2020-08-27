from django.db import models
from Accounts.models import Employee, Form

class Certifacate(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Certificate_To_Request = models.CharField(max_length=60, null=False)
    Others_Certificate = models.CharField(max_length=60, null=True)
    Reason = models.TextField(max_length=150, null=True)
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)
    timeSubmitted = models.TimeField(auto_now=True)
    

    class Meta:
        db_table = 'Certifacate'
    
