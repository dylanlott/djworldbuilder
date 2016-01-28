from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Universe(models.Model): 
	name = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{0}".format(self.name)

class SolarSystem(models.Model):
	name = models.CharField(max_length=100)
	date_created = models.DateTimeField(auto_now_add=True)

	def __str__(self): 
		return "{0}".format(self.name)

class World(models.Model): 
	name = models.CharField(max_length=60)
	date_created = models.DateTimeField(auto_now_add=True)
	climate = models.CharField(max_length=100)
	solar_system = models.ForeignKey(SolarSystem)
	universe = models.ForeignKey(Universe)

	def __str__(self): 
		return "{0}".format(self.name)