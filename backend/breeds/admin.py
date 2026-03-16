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
        "image_url",
    )

    list_filter = (
        "size",
        "housing_type",
    )

    search_fields = ("name",)
