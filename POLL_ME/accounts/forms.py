from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserRegistrationForm(forms.Form):
    username=forms.CharField(label="Username",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password1',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=100)
    password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput(attrs={'class':'form-control'}),max_length=100)

    def clean_email(self):
        data=self.cleaned_data['email']
        filtered_email=User.objects.filter(email=data)
        if filtered_email.exists():
            raise ValidationError('Email Already exist')
        return data
    def  clean(self):
        cleaned_data=super().clean()
        p1=cleaned_data.get('password1')
        p2=cleaned_data.get('password2')
        if p1 and p2:
            if p1 != p2:
                raise ValidationError('Password do not match')




