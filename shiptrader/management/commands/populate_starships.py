import re, json, requests
from django.core.management.base import BaseCommand
from shiptrader.models import *

class Command(BaseCommand):
    help = 'Populate the DB with known sharships'

    def handle(self,*args,**options):
        def cleanse(v):
            v = re.sub(r',','',v)
            return 0 if v == 'unknown' else v

        print('populate_starships')
        url = 'https://swapi.co/api/starships'
        while url:
            ret = requests.get(url)
            print(ret.status_code)
            print(ret.text)
            data = json.loads(ret.text)
            print(data)
            url = data['next']
            for result in data['results']:
                payload = {
                    'starship_class': result['starship_class'],
                    'manufacturer': result['manufacturer'],
                    'length': cleanse(result['length']),
                    'hyperdrive_rating': cleanse(result['hyperdrive_rating']),
                    'cargo_capacity': cleanse(result['cargo_capacity']),
                    'crew': cleanse(result['crew']),
                    'passengers': cleanse(result['passengers']),
                }
                print(payload)
                object = Starship.objects.create(**payload)
