from django import forms
from .models import StudentModel


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['student_firstname', 'student_lastname', 'student_number', 'student_address', 'student_fee']
        widgets = {
            'student_firstname':forms.TextInput(attrs={'class':'form-control'}),
            'student_lastname':forms.TextInput(attrs={'class':'form-control'}),
            'student_number':forms.TextInput(attrs={'class':'form-control'}),
            'student_address':forms.TextInput(attrs={'class':'form-control'}),
            'student_fee':forms.TextInput(attrs={'class':'form-control'}),
        }