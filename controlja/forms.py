from django import forms
from .models import Rutas

class NewRuta(forms.ModelForm):
    class Meta:
        model = Rutas
        fields = '__all__'
