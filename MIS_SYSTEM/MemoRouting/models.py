from django.db import models
from Accounts.models import Employee


class MemoIngoing(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Date = models.DateField()
    Description = models.TextField(max_length=100,null=False)
    Receive_From = models.CharField(max_length=50, null=False)
    Receive_By = models.CharField(max_length=50,null=False)
    
    class Meta:
        db_table = 'MemoIngoing'


class MemoOutgoing(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete=models.CASCADE)
    Date = models.DateField()
    Description = models.TextField(max_length=100,null=False)
    Forwarded_by = models.CharField(max_length=50, null=False)
    Forwarded_to= models.CharField(max_length=50,null=False)
    Received_by = models.CharField(max_length=50,null=False)

    class Meta:
        db_table = 'MemoOutgoing'
