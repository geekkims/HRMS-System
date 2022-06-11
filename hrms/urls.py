from . import views
from django.urls import include, path

urlpatterns = [

      path('',views.home, name="home"),
     path('admin/',views.admin_dashboard, name="admin_dashboard"),
     path('user/',views.employee_dashboard, name="employee_dashboard"),


     
    
]
