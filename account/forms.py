from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from account.models import Account, Profile

class RegistrationForm(UserCreationForm):
    email = forms.CharField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ('email', 'username', 'fullname', 'phone_number', 'address', 'password1' , 'password2')

class LoginForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ('email', 'password')

    def clean(self): #before the form can do anythinh
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        if not authenticate(email = email, password = password):
            raise forms.ValidationError("Please try again.")

class UserUpdateForm(forms.ModelForm):
    email = forms.CharField(max_length=60, help_text='Required. Add a valid email address')

    class Meta:
        model = Account
        fields = ('email', 'username', 'fullname', 'phone_number', 'address')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']