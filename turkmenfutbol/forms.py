from django import forms
from phonenumber_field.modelfields import PhoneNumberField

class HabarlashmakForm(forms.Form):

    at=forms.CharField(max_length=25,
                        widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':"at",
                                'autofocus':'autofocus',
                            }))
    email=forms.EmailField(
                        widget=forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':"email"
                            }))
    title=forms.CharField(max_length=100,
                        widget=forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':"tema"
                            }))
    desc=forms.CharField(
                        widget=forms.Textarea(attrs={
                                'class':'form-control',
                                'style':'resize:none',
                                'placeholder':"tekst"
                            }))