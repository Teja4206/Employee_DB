from django import forms

from app.models import Employee


class Emp_form(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'