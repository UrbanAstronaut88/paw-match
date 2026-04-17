from django.contrib import admin
from .models import Breed


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
        "image_url",
    )

    list_filter = (
        "size",
        "housing_type",
        "kids_friendly",
        "energy",
        "grooming",
    )

    search_fields = ("name",)
