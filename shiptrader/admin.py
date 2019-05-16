from django.contrib import admin
from .forms import *

# Register your models here.

class StarshipAdmin(admin.ModelAdmin):
    form = StarshipForm

class ListingAdmin(admin.ModelAdmin):
    form = ListingForm

admin.site.register(Starship, StarshipAdmin)
admin.site.register(Listing, ListingAdmin)
