from django import forms
from loginapp.models import *


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Signup
