from django import forms

class WorldForm(forms.Form): 
	name = forms.CharField(max_length=100)