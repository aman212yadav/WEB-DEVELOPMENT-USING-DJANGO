from django import forms
from django.contrib.auth.models import User
class ContactForm(forms.Form):
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    Content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class RegisterForm(forms.Form):

    username = forms.CharField( widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data['password']
        confirm_password=cleaned_data['password2']
        if password!=confirm_password:
            raise forms.ValidationError(
                    "Password Mismatched"
                )
    def clean_username(self):
        username=self.cleaned_data['username']
        qs=User.objects.filter(username=username)
        if qs.exists():
            raise  forms.ValidationError('username taken')
        return username  