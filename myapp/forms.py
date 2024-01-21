from django import forms
from . models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'sem', 'branch']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
            'sem':forms.TextInput(attrs={'class':'form-control', 'id':'semid'}),
            'branch':forms.TextInput(attrs={'class':'form-control', 'id':'branchid'})
        }
