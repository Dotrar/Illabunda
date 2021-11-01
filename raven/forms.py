from django import forms
from django.contrib.auth.forms import PasswordResetForm
from . import models

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = models.Resident
        fields = ['email', 'firstname','lastname','house_number']

class RegstrationEmailForm(PasswordResetForm):
    def __init__(self, user, *args, **kwargs):
        self.user=user,
        super().__init__(*args,**kwargs)

    def get_users(self, email):
        return (self.user,)
