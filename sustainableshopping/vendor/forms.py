from django import forms
from people.models import Hacker, Person
from registration.models import Fall2014Registration

class SignupForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.PasswordField()
  