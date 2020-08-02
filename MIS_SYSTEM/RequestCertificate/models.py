from django.db import models
from Accounts.models import Employee

class Certifacate(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Reason = models.TextField

    class Meta:
        db_table = 'Certifacate'
    
