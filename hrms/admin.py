from django.contrib import admin
from hrms.models import Department, EmployeeDetail, Kin

# Register your models here.
admin.site.register([Department,EmployeeDetail,Kin])

