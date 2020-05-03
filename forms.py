from django import forms
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
import datetime


class SignUpForm(forms.Form):
    # TODO: Check the appropriate max length values for  each field.
    first_name = forms.CharField(label='First Name', max_length=256)
    last_name = forms.CharField(label='Last Name', max_length=256)
    email = forms.EmailField(label='E-mail', validators=[EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')
    agree = forms.CharField(label='Agree with Terms', widget=forms.CheckboxInput())

    def clean_email(self):
        # TODO: Cross validate the data with data base and with standards.
        email = self.cleaned_data['email'].lower()
        unq_email = User.objects.get(email=email)
        if unq_email:
            forms.ValidationError(
                "That e-mail is already in use.")

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name'].lower()
        if first_name == '':
            forms.ValidationError(
                "Invalid first name")

    def save(self, commit=True):
        User(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            date_joined= datetime.date
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