from django import forms
from .models import Universe, SolarSystem, World

CLIMATE_CHOICES = (
    ('temperate', 'Temperate'),
    ('arctic', 'Arctic'),
    ('tundra', 'Tundra'),
    ('jungle', 'Jungle'),
    ('volcanic', 'Volcanic'),
)

class WorldForm(forms.Form): 
    name = forms.CharField(max_length=100)
    climate = forms.CharField(max_length=30, 
            widget=forms.Select(choices=CLIMATE_CHOICES))