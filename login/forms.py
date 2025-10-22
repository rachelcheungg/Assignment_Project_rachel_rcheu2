from django import forms
from login.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "username", "first_name", "last_name", "email", "phone_number"

    def clean_first_name(self):
        return self.cleaned_data["first_name"].strip()

    def clean_last_name(self):
        return self.cleaned_data["last_name"].strip()

class UserContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()