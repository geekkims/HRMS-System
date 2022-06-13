from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser



# Create your models here.




# Department

class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name
        


class EmployeeDetail(models.Model):
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    empcode = models.CharField(max_length=50)
    designation = models.CharField(max_length=100, null=True)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    mobile = models.CharField(max_length=15,null=True)
    joiningdate = models.DateTimeField(null=True)
    nhif = models.CharField(max_length=100, null=True)
    nssf = models.CharField(max_length=100, null=True)
    krapin = models.CharField(max_length=100, null=True)
    hudumanumber = models.CharField(max_length=100, null=True)
    idnumber = models.CharField(max_length=10, null=True)
    bank = models.CharField(max_length=100, null=True)
    bankbranch=models.CharField(max_length=100, null=True)
    acnumber=models.CharField(max_length=15,null=True)
    address = models.TextField(max_length=100, default='')
    city=models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    personalemail = models.EmailField(max_length=125, null=False)
    workemail = models.EmailField(max_length=125, null=False)

    def __str__(self):
        return self.first_name+' '+self.last_name
    
          
    def get_absolute_url(self):
        return reverse("hrms:employee_dashboard")

    


class Kin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    employee = models.OneToOneField(EmployeeDetail,on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.first_name+'-'+self.last_name

    def get_absolute_url(self):
        return reverse("hrms:employee_dashboard")



class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(EmployeeDetail, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start




