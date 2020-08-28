from django.db import models
from Accounts.models import Employee,Form

class Cash_Advance(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete = models.CASCADE)
    Cash_Amount = models.BigIntegerField(null=False)
    Reason = models.TextField(max_length=100,null=False)
    FormID = models.ForeignKey(Form,on_delete = models.CASCADE)
    
    class Meta:
        db_table = 'Cash_Advance'

       

  
