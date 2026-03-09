from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    name = models.CharField(max_length=100)

    size = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(3)]
    )

    energy = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    grooming = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    kids_friendly = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    housing = models.CharField(max_length=80)

    def __str__(self):
        return self.name
