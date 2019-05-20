from django.contrib import admin
from .forms import *

# Register your models here.

class StarshipAdmin(admin.ModelAdmin):
    form = StarshipForm
    ordering = ('id',)

class ListingAdmin(admin.ModelAdmin):
    form = ListingForm
    ordering = ('id',)

admin.site.register(Starship, StarshipAdmin)
admin.site.register(Listing, ListingAdmin)
