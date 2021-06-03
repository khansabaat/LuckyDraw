from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Creates a user'

    def add_arguments(self, parser):
        parser.add_argument('username', nargs="?", type=str)
        parser.add_argument('password', nargs="?", type=str)

    def handle(self, *args, **options):
        try:
            user = User.objects.create_user(
                is_staff=False,
                username=options["username"],
                password=options["password"],
            )
            user.save()
        except Exception as e:
            raise CommandError('Could not create user: %s' % str(e))

        self.stdout.write(self.style.SUCCESS('Successfully created user'))
