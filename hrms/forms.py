from unicodedata import name
from django import forms

from hrms.models import Department, EmployeeDetail


# Add Employee Form
class EmployeeForm (forms.ModelForm):
    thumb = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
    last_name = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
    mobile = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Mobile Number'}))
    personalemail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    workemail = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Valid Email'}))
    emergency = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    gender = forms.ChoiceField(choices=EmployeeDetail.GENDER,widget=forms.Select(attrs={'class':'form-control'}))
    nhif = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nhif'}))
    nssf = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'nssf'}))
    krapin = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'KRA Pin'}))
    hudumanumber = forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Huduma Number'}))
    idnumber=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'ID Number'}))
    bank = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    bankbranch = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    acnumber = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Relative Mobile Number'}))
    address=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Permanent Address'}))
    city=forms.CharField(strip=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Permanent Address'}))
    department = forms.ModelChoiceField(Department.objects.all(),required=True, empty_label='Select a department',widget=forms.Select(attrs={'class':'form-control'}))





    class Meta:
        model = EmployeeDetail
        fields = ('first_name','last_name','mobile','personalemail','workemail','emergency','gender','department','nhif','nssf','bank','krapin','idnumber', 'address','thumb','bank','bankbranch','acnumber','hudumanumber')
       