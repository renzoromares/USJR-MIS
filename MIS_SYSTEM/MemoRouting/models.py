from django.db import models
from Accounts.models import Employee, Form


class Memo_Routing(models.Model):
    Id_Number = models.ForeignKey(Employee,on_delete=models.CASCADE)
    FormID = models.ForeignKey(Form,on_delete=models.CASCADE)
    Type_Request = models.CharField(null = False, max_length=100)
    Date_Faculty_Submitted = models.DateTimeField(null = True)
    Date_Chairman_Approved = models.DateTimeField(null = True)
    Date_Dean_Approved = models.DateTimeField(null = True)
    Date_VP_Acad_Approved = models.DateTimeField(null = True)
    Date_President_Approved = models.DateTimeField(null = True)
    Date_PAO_Approved = models.DateTimeField(null = True)
    Date_Accounting_Approved = models.DateTimeField(null = True)
    Date_HR_Approved = models.DateTimeField(null = True)

    class Meta:
        db_table = 'Memo_Routing'