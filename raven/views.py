from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy

from . import forms


class UserRegistrationView(PasswordResetView):
    template_name = "register/register_form.html"
    form_class = forms.RegistrationForm
    email_template_name = "register/registration_email.html"
    subject_template_name = "register/regstration_subject.txt"
    success_url = reverse_lazy("raven:register-done")

    def form_valid(self, form):
        """ """
        self.object = form.save(commit=False)
        # self.object.set_unusable_password()
        self.object.is_active = True
        self.object.save()

        form = forms.RegistrationEmailForm(self.object, self.request.POST)
        form.is_valid()
        return super().form_valid(form)
