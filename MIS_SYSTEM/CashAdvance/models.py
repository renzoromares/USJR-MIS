from django.db import models
from Accounts.models import Form

class Cash_Advance(models.Model):
    Form_ID = models.ForeignKey(Form,on_delete = models.CASCADE)
    Cash_Amount = models.BigIntegerField(null=False)
    Reason = models.TextField(max_length=100,null=False)

