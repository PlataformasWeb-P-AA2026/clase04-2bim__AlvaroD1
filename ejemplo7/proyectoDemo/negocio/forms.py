from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from negocio.models import Restaurante, Chef, Plato, Comentario

class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nombre', 'tipo_cocina', 'capacidad_meses']

class ChefForm(ModelForm):
    class Meta:
        model = Chef
        fields = ['nombres', 'anios_experiencia', 'especialidad_culinaria',
                  'restaurante']

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre_plato', 'descripcion', 'precio_plato',
                  'ingredientes_principales', 'chef']

class ComentarioForm(ModelForm):

    def __init__(self, usuario, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.initial['usuario'] = usuario
        self.fields["usuario"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Comentario
        fields = ['mensaje', 'usuario']

