from django.core.management import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **options):
        # user = User(name='John',
        #             email='test@example.com',
        #             password='secret',
        #             age=25)
        # user = User(name='Neo',
        #             email='test@example.com',
        #             password='secret',
        #             age=58)
        user = User(name='Jack',
                    email='test@example.com',
                    password='secret',
                    age=60)
        ...
        user.save()
        self.stdout.write(f'{user}')
