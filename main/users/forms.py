# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from users.models import Group_chat




class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Email')
    phone = forms.CharField(max_length=15, label='Phone')
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254, label='Email/Phone',
                               widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label='Password', strip=False, widget=forms.PasswordInput)


class ConfirmCodeForm(forms.Form):
    code = forms.CharField(max_length=6, label='Confirmation Code')


#форма для создания групповых чатов
class GroupADD(forms.ModelForm):
    class Meta:
        model = Group_chat
        fields = ['title2', 'title_group', 'photo']
        widgets = {
            'title2': forms.Textarea(attrs={'cols': 47, 'rows': 2}),
            'title_group': forms.Textarea(attrs={'cols': 47, 'rows': 2})
        }