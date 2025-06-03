from django import forms
from .models import stydent 


class stydent_forms(forms.ModelForm):
    class Meta:
        model =stydent
        fields = ['name']