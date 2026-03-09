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
        "housing",
    )

    list_filter = (
        "size",
        "housing",
    )

    search_fields = ("name",)
