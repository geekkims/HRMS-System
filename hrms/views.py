from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrms.decorators import admin_only, allowed_users, unauthenticated_user



# Create your views here.


@login_required(login_url='signin')
def home(request):
    return render(request,"hrms/admin/dashboard.html")

@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
@admin_only
def admin_dashboard(request):
    return render(request,"hrms/admin/dashboard.html")


@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
@admin_only
def employees_details(request):
    
    return render(request,"hrms/admin/employees.html")



@login_required(login_url='signin')
def employee_dashboard(request):
    return render(request,"hrms/employee/dashboard.html")


def add_employee(request):
    return render(request,"hrms/admin/add-employee.html")
  



    

    

