from django import forms

class SignupForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
  