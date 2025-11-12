from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:

        # This is a pre-existing table in Django where we are already storing our internal user's data
        model = User
        fields = ["username", "email", "password1", "password2"]