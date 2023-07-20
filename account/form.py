from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

username_errors = {
    'required':_('required field'),
    'min_length': _('Username must be at least 4 characters long.'),
}
email_errors = {
    'required':_('required field'),
    'invalid': _('Enter a valid email.'),
}
password_errors = {
    'required': _('required field'),
    'min_length': _('Password must be at least 8 characters long.'),
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
            raise forms.ValidationError(_('Passwords do not match.'))
        return cd['password2']

    def clean_username(self):
        cd = self.cleaned_data
        if User.objects.filter(username=cd['username']).exists():
            raise forms.ValidationError(_('There is a registered username with this name.'))
        return cd['username']

    def clean_email(self):
        cd = self.cleaned_data
        if User.objects.filter(email=cd['email']).exists():
            raise forms.ValidationError(_('This email is already registered.'))
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
        

