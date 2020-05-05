from django import forms
from django.core.validators import EmailValidator
from interface.models import User, UserManager
from django.forms import ModelForm
from django import forms
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.contrib.auth import password_validation

"""
class SignUpForm(ModelForm):
    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput())
        fields = ['first_name', 'last_name', 'email', 'password']
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'E-mail',
            'password': 'Password',
        }

"""


class SignUpForm(forms.Form):
    # TODO: Check the appropriate max length values for  each field.
    first_name = forms.CharField(label='First Name', max_length=256)
    last_name = forms.CharField(label='Last Name', max_length=256)
    email = forms.EmailField(label='E-mail', validators=[EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    agree = forms.CharField(label='Agree with Terms', widget=forms.CheckboxInput())
    """
    def clean_email(self):
        # TODO: Cross validate the data with data base and with standards.
        email = self.cleaned_data['email'].lower()

        if User.objects.filter(email=email).first():
            forms.ValidationError(
                "That e-mail is already in use.")

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        if first_name == '':
            forms.ValidationError(
                "Invalid first name")
        return True
    """

    def save(self, commit=True):
        User.objects.create_user(
            email=self.cleaned_data['email'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            password=self.cleaned_data['password']
            ).save()



    # Sample forms.ValidationError()
    """
    if cc_myself and subject:
        # Only do something if both fields are valid so far.
        if "help" not in subject:
            raise forms.ValidationError(
                "Did not send for 'help' in the subject despite "
                "CC'ing yourself."
            )
    """


class SignInForm(forms.Form):
    email = forms.EmailField(label='E-mail', validators=[EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput, label='Password')