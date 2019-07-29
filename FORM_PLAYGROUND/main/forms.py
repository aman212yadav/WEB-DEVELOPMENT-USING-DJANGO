from django import forms

class ExampleForm(forms.Form):
    name=forms.CharField(max_length=256)
    about_me= forms.CharField(widget=forms.Textarea())
    active=forms.BooleanField()