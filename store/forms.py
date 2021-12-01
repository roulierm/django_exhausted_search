from django import forms
from django.forms import ModelForm
from .models import Userpost

class post_user(ModelForm):
    class Meta:
        model = Userpost
        fields = ('Year', 'Mileage', 'Make', 'Model', 'Price', 'email', 'zipCode', 'image')

        labels = {
            'Year': '',
            'Mileage': '',
            'Make': '',
            'Model': '',
            'Price': '',
            'email': '',
            'zipCode': '',
            'image': '',
        }
        widgets = {
            'Year': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Vehicle Year'}),
            'Mileage':forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Miles'}),
            'Make':forms.TextInput(attrs={'class': 'form-control', 'placeholder':' Car Make'}),
            'Model':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Car Model'}),
            'Price':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Car Price'}),
            'email':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':"Seller's Email"}),
            'zipCode':forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Seller"s ZipCode'}),
            'image':forms.FileInput(attrs={'class': 'form-control-file'}),

        }

