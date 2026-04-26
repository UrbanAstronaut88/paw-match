from django.contrib.auth.models import User
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
        BOTH = "Apartment/House", "apartment/house"

    id = models.AutoField(primary_key=True)

    name = models.CharField(max_length=100)

    image_url = models.URLField(blank=True, null=True)

    image = models.ImageField(upload_to="breeds/", blank=True, null=True)

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
        choices=HousingType.choices,
        default=HousingType.BOTH
    )

    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "breed")


class QuizResult(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    size = models.IntegerField()
    energy = models.IntegerField()
    kids = models.IntegerField()
    housing_type = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)


class BreedComparison(models.Model):
    first_breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name="comparisons_as_first"
    )
    second_breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name="comparisons_as_second"
    )
    conclusion = models.TextField(max_length=450)

    class Meta:
        unique_together = ("first_breed", "second_breed")

    def __str__(self) -> str:
        return f"{self.first_breed.name} vs {self.second_breed.name}"
