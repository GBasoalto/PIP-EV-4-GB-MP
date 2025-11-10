from django import forms
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": "Usuario o contraseña incorrectos. Por favor vuelva a intentar.",
        "inactive": "Esta cuenta esta inactiva. Contacta al administrador.",
    }
