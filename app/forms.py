from django import forms
from .models import JoinForm

class JoinFormForm(forms.ModelForm):
    class Meta:
        model = JoinForm
        fields = ['name', 'age', 'dob', 'phone', 'address', 'email', 'department', 'course', 'purpose', 'materials_provide']
