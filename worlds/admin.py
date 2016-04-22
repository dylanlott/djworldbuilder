from django.contrib import admin

# Register your models here.
from models import World, SolarSystem, Universe

admin.site.register(World)
admin.site.register(SolarSystem)
admin.site.register(Universe)