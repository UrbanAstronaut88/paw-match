from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Create superuser automatically"

    def handle(self, *args, **kwargs):
        email = "root@pawmatch.com"
        password = "StrongPass123?"

        if not User.objects.filter(email=email).exists():
            user = User.objects.create_superuser(
                username=email,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        else:
            self.stdout.write("Superuser already exists")
