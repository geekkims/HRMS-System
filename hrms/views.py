from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from hrms.decorators import unauthenticated_user
# from authentication.decorators import unauthenticated_user


# Create your views here.


@login_required(login_url='signin')
def home(request):
    return render(request,"hrms/admin/dashboard.html")

@login_required(login_url='signin')
@unauthenticated_user
def admin_dashboard(request):
    return render(request,"hrms/admin/dashboard.html")

@login_required(login_url='signin')
def employee_dashboard(request):
    return render(request,"hrms/employee/dashboard.html")
    

