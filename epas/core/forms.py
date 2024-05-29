
from django import forms
from django.forms import ModelForm
from .models import Employee, Metric

class EmpForm(ModelForm):
    empno = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Employee Number'}))
    fname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    lname = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    department = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Department'}))
    class Meta:
        model = Employee
        fields = [ 'empno','fname','lname','department','dp']

class MetricForm(ModelForm):
    class Meta:
        model = Metric
        fields = ['check_in', 'check_out', 'error_rate', 'submission_status']
        labels = {
            'submission_status': 'submission_status',
        }