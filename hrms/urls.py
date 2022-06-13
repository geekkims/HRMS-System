from . import views
from django.urls import include, path


app_name = 'hrms'
urlpatterns = [

     # Admin Functions

     path('admin/',views.admin_dashboard, name="admin_dashboard"),
     
    

     # Employee Links
#      All employees
     path('employees-details/',views.employee_dashboard.as_view(), name="employee_dashboard"),


     # Add Employee


      path('add-employee/',views.Employee_New.as_view(), name="employee_new"),


     
    
]
