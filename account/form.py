from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

username_errors = {
    'required':'required field',
    'min_length': 'Username must be at least 4 characters long.',
}
email_errors = {
    'required':'required field',
    'invalid': 'Enter a valid email.',
}
password_errors = {
    'required': 'required field',
    'min_length': 'Password must be at least 8 characters long.',
}


class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    
    class Meta:
        model=User
        fields = [
                'username',
                'email',
                'password1',
                'password2'
            ]
        
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError('There is a registered username with this name.')
        return cd['username']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError('This email is already registered.')
        return cd['email']



class ContactForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']
        

