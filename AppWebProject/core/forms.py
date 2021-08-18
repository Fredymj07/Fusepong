from django import forms
from django.core.validators import EmailValidator
from .models import DocumentType

class AddClientForm(forms.Form):
    name = forms.CharField(label='Nombre', min_length=3, max_length=14, required=True)
    last_name = forms.CharField(label='Apellido', min_length=3, max_length=14, required=False)
    address = forms.CharField(label='Dirección', min_length=15, max_length=100, required=True)
    document_type = forms.ModelChoiceField(label='Tipo de Documento', queryset=DocumentType.objects.all(), required=True)
    document_number = forms.CharField(label='Número de Documento', min_length=6, max_length=14, required=True)
    phone = forms.CharField(label='Teléfono', min_length=7, max_length=10, required=True)
    email = forms.CharField(label='Correo', validators=[EmailValidator(message='Correo inválido', whitelist='mail, gmail, outlook, hotmail, yahoo')], required=True)