from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="hakuro.lucas@gmail.com").exists():
            User.objects.create_superuser("hakuro.lucas@gmail.com", "hakuro.lucas@gmail.com", "hakuro")
