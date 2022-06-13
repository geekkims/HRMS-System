from . import views
from django.urls import include, path


app_name = 'hrms'
urlpatterns = [

     # Admin Functions

     path('admin/',views.admin_dashboard, name="admin_dashboard"),
     path('employees-details/',views.employees_details, name="employees_details"),
    







     # Employee Dashboard
     path('user/',views.employee_dashboard, name="employee_dashboard"),


     # Add Employee


      path('add-employee/',views.Employee_New.as_view(), name="employee_new"),


     
    
]
