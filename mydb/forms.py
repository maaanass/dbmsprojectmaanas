from django import forms
from .models import employee
from .models import members

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'
class memberForm(forms.ModelForm):
    class Meta:
        model = members
        fields = '__all__'