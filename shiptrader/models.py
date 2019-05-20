from django.db import models


class Starship(models.Model):
    def __str__(self):
        return str(self.id)+': ' + self.starship_class + '/' + self.manufacturer

    starship_class = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)

    length = models.FloatField()
    hyperdrive_rating = models.FloatField()
    cargo_capacity = models.BigIntegerField()

    crew = models.IntegerField()
    passengers = models.IntegerField()


class Listing(models.Model):
    def __str__(self):
        return str(self.id) + ': ' + self.name

    name = models.CharField(max_length=255)
    ship_type = models.ForeignKey(Starship, related_name='listings')
    price = models.IntegerField()
    created = models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=True)
