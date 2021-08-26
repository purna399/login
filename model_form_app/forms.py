from .models import EmpPersonal
from django import forms 

class EmpPersonalModelForm(forms.ModelForm):
    class Meta:
        model = EmpPersonal
        fields = '__all__'


class EmpPersonalForm(forms.Form):
    name      =  forms.CharField(max_length=20)
    mobile    =  forms.CharField(max_length=10)
    per_email =  forms.CharField(max_length=20)
    age       =  forms.IntegerField()
    address   =  forms.CharField(max_length=20)
    country   =  forms.CharField(max_length=10)


    


