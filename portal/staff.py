from django import forms

from .models import Staff

class StaffForm(forms.ModelForm):

    class Meta:
        model = Staff
        fields = ('staffid', 'name', 'department', 'email', 'phone', 'complain')