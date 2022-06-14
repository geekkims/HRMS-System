from unicodedata import name
from django import forms
import time
from hrms.models import Attendance, Department, EmployeeDetail, Kin
from django.db.models import Q
from django.utils import timezone




# Add Employee Form
class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    empcode=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Payroll Number'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    joiningdate=forms.DateInput(attrs={'class':'form-control','type':'date'}),
    personalemail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    workemail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=EmployeeDetail.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    nhif = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nhif'}))
    nssf = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nssf'}))
    krapin = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'KRA Pin'}))
    hudumanumber = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Huduma Number'}))
    idnumber=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ID Number'}))
    bank = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name of the Bank'}))
    bankbranch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Bank Branch'}))
    acnumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Account Number'}))
    address=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Permanent Address'}))
    city=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Permanent Address'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))





    class Meta:
        model = EmployeeDetail
        fields = ('first_name','last_name','empcode' ,'joiningdate','mobile','personalemail','workemail','emergency','gender','department','nhif','nssf','krapin','idnumber', 'address','thumb','bank','bankbranch','acnumber','hudumanumber')
       

# Kin Update Details


class KinForm(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    employee = forms.ModelChoiceField(EmployeeDetail.objects.filter(kin__employee=None),required=False,widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Kin
        fields = '__all__'



class AttendanceForm(forms.ModelForm):
    status = forms.ChoiceField(choices=Attendance.STATUS,widget=forms.Select(attrs={'class':'form-control w-50'}))
    staff = forms.ModelChoiceField(EmployeeDetail.objects.filter(Q(attendance__status=None) | ~Q(attendance__date = timezone.localdate())), widget=forms.Select(attrs={'class':'form-control w-50'}))
    class Meta:
        model = Attendance
        fields = ['status','staff']