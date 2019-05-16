from django import forms
from .models import *

class StarshipForm(forms.ModelForm):
    class Meta:
        model = Starship
        fields = '__all__'

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'