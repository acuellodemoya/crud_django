from  django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control m-3'}))
    apellido = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control m-3'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control m-3'}))
    numero_celular = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control m-3'}))
    




