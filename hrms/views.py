from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrms.decorators import admin_only, allowed_users, unauthenticated_user
from django.views.generic import FormView, CreateView
from hrms.forms import EmployeeForm
from hrms.models import EmployeeDetail
from django.contrib.auth.mixins import LoginRequiredMixin




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



  


# Employee's Controller


class Employee_New(LoginRequiredMixin,CreateView):
    model = EmployeeDetail  
    form_class = EmployeeForm  
    template_name = 'hrms/admin/add-employee.html'
    login_url = 'authentication:signin'
    redirect_field_name = 'redirect:'
    

    

