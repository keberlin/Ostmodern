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
        'ship_type': object.ship_type.id,
        'price': object.price,
        'activate': object.activate,
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
        data = request.GET
        pk = data['id']
        object = Listing.objects.get(pk=pk)
        response = listing_struct(object)
        return JsonResponse(response)

    def post(self,request):
        data = request.POST
        payload = {
            'name': data['name'],
            'ship_type': Starship.objects.get(pk=data['ship_type']),
            'price': data['price'],
        }
        object = Listing.objects.create(**payload)
        response = {}
        return JsonResponse(response,status=201)

    def delete(self,request):
        data = request.GET
        pk = data['id']
        object = Listing.objects.delete(pk=pk)
        response = {}
        return JsonResponse(response)


class ListingsView(View):
    def get(self,request):
        data = request.GET
        if 'starship_class' in data:
            objects = Listing.objects.filter(ship_type__starship_class=data['starship_class'])
        else:
            objects = Listing.objects.all()
        objects = objects.order_by('created')
        structs = []
        for object in objects:
            structs.append(listing_struct(object))
        response = {'listings':structs}
        return JsonResponse(response)


class ActivateView(View):
    def get(self,request):
        data = request.GET
        pk = data['id']
        object = Listing.objects.get(pk=pk)
        object.activate = True
        object.save()
        response = {}
        return JsonResponse(response)


class DeactivateView(View):
    def get(self,request):
        data = request.GET
        pk = data['id']
        object = Listing.objects.get(pk=pk)
        object.activate = False
        object.save()
        response = {}
        return JsonResponse(response)
