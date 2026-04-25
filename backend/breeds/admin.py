from django.contrib import admin
from .models import Breed, BreedComparison


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "size",
        "energy",
        "grooming",
        "kids_friendly",
        "housing_type",
        "image",
    )

    list_filter = (
        "size",
        "housing_type",
        "kids_friendly",
        "energy",
        "grooming",
    )

    search_fields = ("name",)


@admin.register(BreedComparison)
class BreedComparisonAdmin(admin.ModelAdmin):
    list_display = ("first_breed", "second_breed")
    search_fields = ("first_breed__name", "second_breed__name", "conclusion")
