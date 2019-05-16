from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.generic import View
from .models import *

# Create your views here.

def starship_struct(object):
    return {
        'id': object.id,
        'starship_class': object.starship_class,
        'manufacturer': object.manufacturer,
        'length': object.length,
        'hyperdrive_rating': object.hyperdrive_rating,
        'cargo_capacity': object.cargo_capacity,
        'crew': object.crew,
        'passengers': object.passengers,
    }

def listing_struct(object):
    return {
        'id': object.id,
        'name': object.name,
        'ship_type': object.ship_type.starship_class,
        'price': object.price,
    }

class StarshipView(View):
    def get(self,request):
        data = request.GET
        pk = data['id']
        object = Starship.objects.get(pk=pk)
        response = starship_struct(object)
        return JsonResponse(response)

    def post(self,request):
        data = request.POST
        payload = {
            'starship_class': data['starship_class'],
            'manufacturer': data['manufacturer'],
            'length': data['length'],
            'hyperdrive_rating': data['hyperdrive_rating'],
            'cargo_capacity': data['cargo_capacity'],
            'crew': data['crew'],
            'passengers': data['passengers'],
        }
        object = Starship.objects.create(**payload)
        response = {}
        return JsonResponse(response,status=201)

    def delete(self,request):
        data = request.GET
        pk = data['id']
        object = Starship.objects.delete(pk=pk)
        response = {}
        return JsonResponse(response)

class StarshipsView(View):
    def get(self,request):
        structs = []
        objects = Starship.objects.all()
        for object in objects:
            structs.append(starship_struct(object))
        response = {'starships':structs}
        return JsonResponse(response)

class ListingView(View):
    def get(self,request):
        response = {'ListingView':'GET'}
        return JsonResponse(response)

    def post(self,request):
        response = {'ListingView':'POST'}
        return JsonResponse(response)

    def delete(self,request):
        response = {'ListingView':'DELETE'}
        return JsonResponse(response)

class ListingsView(View):
    def get(self,request):
        structs = []
        objects = Listing.objects.all()
        for object in objects:
            structs.append(listing_struct(object))
        response = {'listings':structs}
        return JsonResponse(response)
