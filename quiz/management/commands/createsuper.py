from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates a superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='adem').exists():
            User.objects.create_superuser('adem', 'adem@example.com', 'adem123')
            self.stdout.write(self.style.SUCCESS('Superuser created successfully'))
        else:
            self.stdout.write('Superuser already exists')