from django import forms
from.models import Details

class MemberForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['message','name','email','subject']
