from . import views
from django.urls import include, path

urlpatterns = [

     # Admin Functions

     path('admin/',views.admin_dashboard, name="admin_dashboard"),
     path('employees-details/',views.employees_details, name="employees_details"),
     path('add-employee/',views.add_employee, name="add_employee"),







     # Employee Dashboard
     path('user/',views.employee_dashboard, name="employee_dashboard"),


     
    
]
