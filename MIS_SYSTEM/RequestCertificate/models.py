from django.db import models
from Accounts.models import Form

class Certifacate(models.Model):
    Form_ID = models.ForeignKey(Form,on_delete=models.CASCADE)
    Reason = models.TextField
    
