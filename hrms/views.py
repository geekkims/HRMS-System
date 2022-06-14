from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import View
from hrms.decorators import admin_only, allowed_users, unauthenticated_user
from django.views.generic import FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from hrms.forms import AttendanceForm, DepartmentForm, EmployeeForm, KinForm, LeaveForm, RecruitmentForm
from hrms.models import Attendance, Department, EmployeeDetail, Kin, Leave, Recruitment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q


# Create your views here.


@login_required(login_url='signin')
def home(request):
    return render(request,"hrms/admin/dashboard.html")

@login_required(login_url='signin')
@allowed_users(allowed_roles=['admin'])
@admin_only
def admin_dashboard(request):
    return render(request,"hrms/admin/dashboard.html")



# Employee's Controller


class Employee_New(LoginRequiredMixin,CreateView):
    model = EmployeeDetail  
    form_class = EmployeeForm  
    template_name = 'hrms/admin/add-employee.html'
    login_url = 'authentication:signin'
    redirect_field_name = 'redirect:'


class employee_dashboard(LoginRequiredMixin,ListView):
    model = EmployeeDetail
    template_name = 'hrms/admin/employees.html'
    login_url = 'authentication:signin'
    context_object_name = 'employees'
    paginate_by  = 10


# Single Employee View

class Employee_View(LoginRequiredMixin,DetailView):
    queryset = EmployeeDetail.objects.select_related('department')
    template_name = 'hrms/admin/employee-single.html'
    context_object_name = 'employee'
    login_url = 'authentication:signin'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context


class Employee_Update(LoginRequiredMixin,UpdateView):
    model = EmployeeDetail
    template_name = 'hrms/admin/editemployee.html'
    form_class = EmployeeForm
    login_url = 'authentication:signin'
    
    
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (LoginRequiredMixin,CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/admin/kin_add.html'
    login_url = 'hrms:login'

class Employee_Kin_Update(LoginRequiredMixin,UpdateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/admin/kin_update.html'
    login_url = 'hrms:login'

    def get_initial(self):
        initial = super(Employee_Kin_Update,self).get_initial()
        
        if 'id' in self.kwargs:
            emp =  EmployeeDetail.objects.get(pk=self.kwargs['id'])
            initial['employee'] = emp.pk
            
            return initial
   


#Attendance View

class Attendance_New (LoginRequiredMixin,CreateView):
    model = Attendance
    form_class = AttendanceForm
    login_url = 'hrms:login'
    template_name = 'hrms/attendance/create.html'
    success_url = reverse_lazy('hrms:attendance_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["today"] = timezone.localdate()
        pstaff = Attendance.objects.filter(Q(status='PRESENT') & Q (date=timezone.localdate())) 
        context['present_staffers'] = pstaff
        return context


class Attendance_Out(LoginRequiredMixin,View):
    login_url = 'hrms:login'

    def get(self, request,*args, **kwargs):

       user=Attendance.objects.get(Q(staff__id=self.kwargs['pk']) & Q(status='PRESENT')& Q(date=timezone.localdate()))
       user.last_out=timezone.localtime()
       user.save()
       return redirect('hrms:attendance_new')   





class LeaveNew (LoginRequiredMixin,CreateView, ListView):
    model = Leave
    template_name = 'hrms/leave/create.html'
    form_class = LeaveForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:leave_new')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["leaves"] = Leave.objects.all()
        return context


#Department views

class Department_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = EmployeeDetail.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'hrms/department/create.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:attendance_new')

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:attendance_new')



class RecruitmentNew (CreateView):
    model = Recruitment
    template_name = 'hrms/recruitment/index.html'
    form_class = RecruitmentForm
    success_url = reverse_lazy('hrms:recruitment')

class RecruitmentAll(LoginRequiredMixin,ListView):
    model = Recruitment
    login_url = 'hrms:login'
    template_name = 'hrms/recruitment/all.html'
    context_object_name = 'recruit'

class RecruitmentDelete (LoginRequiredMixin,View):
    login_url = 'hrms:login'
    def get (self, request,pk):
     form_app = Recruitment.objects.get(pk=pk)
     form_app.delete()
     return redirect('hrms:recruitmentall', permanent=True)