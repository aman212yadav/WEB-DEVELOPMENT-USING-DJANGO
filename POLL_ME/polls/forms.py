from django import forms
from polls import models

class PollForm(forms.ModelForm):
    choice1=forms.CharField(label="First choice",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    choice2=forms.CharField(label="Second choice",max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=models.Poll
        fields=['text']
        widgets = {
            'text': forms.Textarea(attrs={'cols': 73, 'rows': 5}),
         
        }
class EditPollForm(forms.ModelForm):
    class Meta:
        model=models.Poll
        fields=['text']
        widgets = {
            'text': forms.Textarea(attrs={'class':'form-control','cols': 73, 'rows': 5})

        }        
class ChoiceForm(forms.ModelForm):
    class Meta:
        model=models.Choice
        fields=['choice_text']        