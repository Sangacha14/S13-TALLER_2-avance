from datetime import datetime

from django import forms
from django.forms import ModelForm

from aplicaciones.core.models import Pais
from aplicaciones.ventas.models import Cliente, Factura


class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude=['usuario']

        widgets = {
            'ruc': forms.TextInput(attrs={'class': 'form-control','placeholder':'ingrese ruc'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            # 'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'foto': forms.ImageField(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        }

class VentaForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cliente'].widget.attrs['autofocus'] = True
        self.fields['subtotal'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['iva'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['total'].widget.attrs = {'disabled':True,'class':'form-control'}
    class Meta:
        model = Factura
        fields = '__all__'
        widgets = {
          'fecha': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d'),}
          ),
        }

