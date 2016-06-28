from django import forms
from .models import Rutas,  Comentario

class NewRuta(forms.ModelForm):
    class Meta:
        model = Rutas
        fields = '__all__'
        
class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        exclude = ["ruta"]
