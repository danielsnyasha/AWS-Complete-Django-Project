from django import forms
from.models import Details

class DetailsForm(forms.Modelform):
    class Meta:
        model = Details
        fields = ['message', 'name','email','subject']
