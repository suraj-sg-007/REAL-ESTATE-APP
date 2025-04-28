from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Listing

class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [  
          'title',
          'price',
          'num_bedrooms',
          'num_bathrooms',
          'square_footage',
          'address',
          'image',
        ]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("Passwords do not match")
        return password_confirm
