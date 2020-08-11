from django.db import models
from Accounts.models import Employee

class Certifacate(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Certificate_To_Request = models.CharField(max_length=60, null=False)
    Others_Certificate = models.CharField(max_length=60, null=True)
    Reason = models.TextField(max_length=150, null=True)
    

    class Meta:
        db_table = 'Certifacate'
    
