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
#Single Employee
     path('employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
     path('employee/<int:pk>/update/', views.Employee_Update.as_view(), name='employee_update'),
     path('employee/<int:pk>/delete/', views.Employee_Delete.as_view(), name='employee_delete'),
     path('employee/<int:id>/kin/add/', views.Employee_Kin_Add.as_view(), name='kin_add'),
     path('employee/<int:id>/kin/<int:pk>/update/', views.Employee_Kin_Update.as_view(), name='kin_update'),

#Attendance Routes
    path('dashboard/attendance/in/', views.Attendance_New.as_view(), name='attendance_new'),
    path('dashboard/attendance/<int:pk>/out/', views.Attendance_Out.as_view(), name='attendance_out'),
#Leave Routes
    path("dashboard/leave/new/", views.LeaveNew.as_view(), name="leave_new"),

#Department Routes
    path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
    path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'), 



#Recruitment

    path("recruitment/",views.RecruitmentNew.as_view(), name="recruitment"),
    path("recruitment/all/",views.RecruitmentAll.as_view(), name="recruitmentall"),
    path("recruitment/<int:pk>/delete/", views.RecruitmentDelete.as_view(), name="recruitmentdelete"),  
    
]
