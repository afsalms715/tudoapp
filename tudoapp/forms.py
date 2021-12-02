from django import forms

from tudoapp.models import tudo


class toduModel(forms.ModelForm):
    class Meta:
        model = tudo
        fields ='__all__'