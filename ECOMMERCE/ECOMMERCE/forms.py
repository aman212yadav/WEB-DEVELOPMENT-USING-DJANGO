from django import forms

class ContactForm(forms.Form):
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    Content=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))