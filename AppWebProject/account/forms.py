from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nombres', min_length=3, max_length=50, error_messages={'Invalid':'El nombre ingresado no cumple con los parámetros necesarios.'})
    last_name = forms.CharField(label='Apellidos', min_length=4, max_length=70, error_messages={'Invalid':'El apellido no cumple con los parámetros necesarios.'})
    email = forms.EmailField(label='Email', max_length=50, help_text='Ingresa tu correo electrónico', error_messages={'Invalid':'La dirección de correo ingresada no es válida.'})

    """ Este método permite validar si un email ingresado ya se encuentra registrado en la base de datos """
    def clean_email(self):
        email_user = self.cleaned_data['email'].lower()
        user_data = User.objects.filter(email=email_user)
        if user_data.count():
            raise ValidationError('El email ingresado ya se encuentra registrado.')
        return email_user

    """ Este método permite validar si el nombre de usuario ingresado ya se encuentra registrado en la base de datos """
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        data = User.objects.filter(username=username)
        if data.count():
            raise  ValidationError("El usuario ingresado ya se encuentra registrado en la plataforma")
        return username

    """ Este método permite sobreescibir el método guardar, de acuerdo con el campo (email) agregado al formulario """
    def save(self, commit=True):
        user_data = User.objects.create_user(
            self.cleaned_data['username'],
            first_name = self.cleaned_data['first_name'],
            last_name = self.cleaned_data['last_name'],
            email = self.cleaned_data['email'],
            password = self.cleaned_data['password1'],
        )
        return user_data