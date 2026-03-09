from django.db import models


class Breed(models.Model):
    name = models.CharField(max_length=100)

    size = models.IntegerField()
    energy = models.IntegerField()
    grooming = models.IntegerField()
    kids_friendly = models.IntegerField()

    housing = models.CharField(max_length=50)

    def __str__(self):
        return self.name
