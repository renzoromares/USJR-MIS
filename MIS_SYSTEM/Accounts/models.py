from django.db import models

class Employee(models.Model):
    Id_Number = models.IntegerField(primary_key=True, null=False)
    First_Name = models.TextField(max_length=50, null=False)
    Last_Name = models.TextField(max_length=50, null=False)
    Email = models.TextField(max_length=100, null=False)
    Contact = models.BigIntegerField(null=False)
    Password = models.CharField(max_length=20, null=False)
    Employee_Picture = models.ImageField(upload_to='pictures',null=True)

    class Meta:
        db_table = 'Employee'
    
    def __str__(self):
        return "%s %s %s %s %s" % (self.First_Name, self.Email, self.Id_Number, self.Contact, self.Last_Name)


class Department(models.Model):
    Department_ID = models.AutoField(primary_key=True)
    Id_Number = models.ForeignKey(Employee, on_delete = models.CASCADE)
    department = models.CharField(max_length=100, null=False)  
    College = models.CharField(max_length=100, null=False)  
    Status_Dept = models.TextField(max_length=100, null=False)

    class Meta:
        db_table = 'Department'

    def __str__(self):
        return "%s %s" % (self.department, self.Status_Dept)

    

class Form(models.Model):
    Form_ID = models.AutoField(primary_key=True)
    Id_Number = models.ForeignKey(Employee, on_delete = models.CASCADE)
    Type = models.CharField(max_length=50,null=False)
    Date_Requested = models.DateField(null = True)
    Date_Approved = models.DateField(null = True) 
    Status = models.CharField(max_length=20, null=False)

    class Meta:
        db_table = 'Form'



#dataForm=Department.objects.raw('Select * From "Department" Natural Join "Form"')
#dataForm=Form.objects.prefetch_related('Id_Number').get(Id_Number = '2015023657')


    