from django import forms
from Schoolapp.models import Student

class Schoolform(forms.ModelForm):
    class Meta:
        model=Student
        fields=('Name','div','address','phone_number')