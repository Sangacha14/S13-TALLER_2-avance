from datetime import datetime

from django import forms
from django.forms import ModelForm

from aplicaciones.core.models import Pais
from aplicaciones.ausentismo.models import Empleado,Permiso,PermisoVacaciones


class EmpleadoFormulario(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        exclude=['usuario']

        widgets = {

            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese cedula'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ingrese cargo'}),
            'telefonos': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.Select(attrs={'class': 'form-control'}),
            'provincia': forms.Select(attrs={'class': 'form-control'}),
            'ciudad': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            # 'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(format=('%d/%m/%Y'),
                                                attrs={'class': 'form-control', 'placeholder': 'Seleccione una fecha', 'type': 'date'}),

            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            # 'foto': forms.ImageField(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control'}),
        }

class PermisoFormulario(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['empleado'].widget.attrs['autofocus'] = True
        self.fields['motivo_permiso'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['dias_permiso'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['estado'].widget.attrs = {'disabled':True,'class':'form-control'}
    class Meta:
        model = Permiso
        fields = '__all__'
        widgets = {
          'fecha': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d'),}
          ),
        }
class PermisoVacacionesFormulario(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['empleado'].widget.attrs['autofocus'] = True
        self.fields['motivo_permiso'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['dias_permiso'].widget.attrs = {'readonly':True,'class':'form-control'}
        self.fields['estado'].widget.attrs = {'disabled':True,'class':'form-control'}
    class Meta:
        model = PermisoVacaciones
        fields = '__all__'
        widgets = {
          'fecha': forms.DateInput(
                         format=('%Y-%m-%d'),
                         attrs={'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d'),}
          ),
        }

