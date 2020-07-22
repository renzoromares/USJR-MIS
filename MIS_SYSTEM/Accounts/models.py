from django.db import models

# Create your models here.
class Employee(models.Model):
    Id_Number = models.CharField(max_length=20, primary_key=True, null=False)
    Full_Name = models.TextField(max_length=100, null=False)
    Email = models.TextField(max_length=100, null=False)
    Contact = models.BigIntegerField(null=False)
    Password = models.CharField(max_length=20, null=False)
    
    def __str__(self):
        return "%s %s %s %s" % (self.Full_Name, self.Email, self.Id_Number, self.Contact)
        

class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True, default=100)
    Id_Number = models.ForeignKey(Employee, on_delete = models.CASCADE)
    department = models.CharField(max_length=100, null=False)  
    Status_Dept = models.TextField(max_length=100, null=False)
    
    def __str__(self):
        return "%s %s" % (self.department, self.Status_Dept)
    