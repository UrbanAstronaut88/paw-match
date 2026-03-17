from django.db import models


class Breed(models.Model):
    class Size(models.IntegerChoices):
        SMALL = 1, "small"
        MEDIUM = 2, "medium"
        LARGE = 3, "large"


    class Rating(models.IntegerChoices):
        VERY_LOW = 1, "very low"
        LOW = 2, "low"
        MEDIUM = 3, "medium"
        HIGH = 4, "high"
        VERY_HIGH = 5, "very high"


    class HousingType(models.TextChoices):
        APARTMENT = "Apartment", "apartment"
        HOUSE = "House", "house"
        BOTH = "both", "apartment and house"

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

    image_url = models.URLField(blank=True, null=True)

    size = models.IntegerField(
        choices=Size.choices
    )

    energy = models.IntegerField(
        choices=Rating.choices
    )

    grooming = models.IntegerField(
        choices=Rating.choices
    )

    kids_friendly = models.IntegerField(
        choices=Rating.choices
    )

    housing_type = models.CharField(
        max_length=20,
        choices=HousingType.choices,
        default=HousingType.BOTH
    )

    description = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.name
