from django import forms

from .models import Parent

class ParentForm(forms.ModelForm):

    class Meta:
        model = Parent
        fields = ('studentName', 'usn', 'semester', 'name', 'email', 'phone', 'complain')
