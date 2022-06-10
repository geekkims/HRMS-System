from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='signin')
def admin_dashboard(request):
    return render(request,"hrms/admin/dashboard.html")

@login_required(login_url='signin')
def employee_dashboard(request):
    return render(request,"hrms/employee/dashboard.html")
    

