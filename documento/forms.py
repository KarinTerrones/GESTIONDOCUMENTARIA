from cProfile import label
import email
from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm,Select
from documento.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(max_length=80)

    class Meta:
        model = Account
        fields = ['email','username','password1','password2']
        labels = {
            'username':'Usuario'
        }


class LoginForm(forms.ModelForm):

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    
    class  Meta:
        model = Account
        fields = {'email','password'}
    def clean(self):
        email= self.cleaned_data['email']
        password=self.cleaned_data['password']
        if not authenticate(email=email,password=password):
            raise forms.ValidationError('Login Invalido')


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ["nombre","tipo","proveedor","pedido"]
        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'pedido' : forms.Textarea(attrs={'class':'form-control'}),
        }

class PerfilEncargado(forms.ModelForm):

    class Meta:
        model = EncargadoArea
        fields = ["nombre","apellido_pater","apellido_mater","celular","foto_perfil"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_pater" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_mater" : forms.TextInput(attrs={'class':'form-control'}),
            "celular" : forms.TextInput(attrs={'class':'form-control'}),
            "foto_perfil" : forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
            "nombre" : "Nombre",
            "apellido_pater":"Apellido Paterno",
            "apellido_mater" :"Apellido Materno",
            "celular" : "Celular",
            "foto_perfil" : "Foto de Perfil",

        }

class Editar_Encargado(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["nombre"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class':'form-control'}),
        }
        label = {
            "nombre":"Nueva Area", 
        }

class EditarProveedor(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['razon_social','contacto','categoria']
        widgets = {
            'razon_social' : forms.TextInput(attrs={'class':'form-control'}),
            'contacto' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : Select(attrs={'class':'form-control'}),
        }
        labels = {
            'razon_social':"Razon Social",
            'contacto': "Contacto",
            'categoria':"Categoria",
        }

class RegistarProveedor(forms.ModelForm):

    class Meta:
        model = Proveedor
        fields = ['razon_social','ruc','contacto','categoria']
        widgets = {
            'razon_social' : forms.TextInput(attrs={'class':'form-control'}),
            'ruc' : forms.TextInput(attrs={'class':'form-control'}),
            'contacto' : forms.TextInput(attrs={'class':'form-control'}),
            'categoria' : Select(attrs={'class':'form-control'}),
        }
        labels = {
            'razon_social':"Razon Social",
            'ruc':'Ruc',
            'contacto': "Contacto",
            'categoria':"Categoria",
        }

class RegistrarFactura(forms.ModelForm):

    class Meta:
        model = Factura
        fields = "__all__"
        widgets = {
            "proveedor": Select(attrs={'class':'form-control'}),
            'area': Select(attrs={'class':'form-control'}),
            'archivo': forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
            'proveedor': "Proveedor",
            'area': 'Area',
            'archivo': "Archivo"
        }

class EditarFactura(forms.ModelForm):
    class Meta:
        model = Factura
        fields = "__all__"
        widgets = {
            "proveedor": Select(attrs={'class':'form-control'}),
            'area': Select(attrs={'class':'form-control'}),
            'archivo': forms.FileInput(attrs={'class':'form-control'}),
        }
        labels = {
            'proveedor': "Proveedor",
            'area': 'Area',
            'archivo': "Factura"
        }

class RegistrarEncargado(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'encargado': Select(attrs={'class':'form-control'}),
        }
        labels = {
            'nombre' : "Area",
            'encargado' : "Encargado Area"
        }

class RegistrarPerfilEncargado(forms.ModelForm):

    email=forms.ModelChoiceField(queryset=Account.objects.filter(groups=4),widget=Select(attrs={'class':'form-control'}))

    class Meta:
        model = EncargadoArea
        fields = ['email',"nombre","apellido_pater","apellido_mater","celular"]
        widgets = {
            "nombre" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_pater" : forms.TextInput(attrs={'class':'form-control'}),
            "apellido_mater" : forms.TextInput(attrs={'class':'form-control'}),
            "celular" : forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            "email": "Correo",
            "nombre" : "Nombre",
            "apellido_pater":"Apellido Paterno",
            "apellido_mater" :"Apellido Materno",
            "celular" : "Celular",

        }
class EditarSolicitud(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ["estado"]
        widgets = {
            'estado':Select(attrs={'class':'form-control'}),
        }
        labels = {
            "estado":"Estado"
        }