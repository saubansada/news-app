from django.core.management.base import BaseCommand
from apps.users.models import ApplicationUser, Role
from django.core.exceptions import ObjectDoesNotExist
from mongoengine import DoesNotExist

class Command(BaseCommand):
    help = 'Creates an initial superuser with role-based access control'

    def add_arguments(self, parser):
        # Arguments for username, email, password, and role
        #parser.add_argument('username', type=str, help='Username for the initial user')
        parser.add_argument('email', type=str, help='Email for the initial user')
        parser.add_argument('password', type=str, help='Password for the initial user')

    def handle(self, *args, **kwargs):
        # Extract command-line arguments
        #uname = kwargs['username']
        email = kwargs['email']
        password = kwargs['password']
        #self.stdout.write(self.style.SUCCESS(f"Creating user with username: {uname}, email: {email}"))

        # Create roles first
        admin_role = Role(name='admin', description='Admin role')
        admin_role.save()
        
        # Create the initial superuser
        user = ApplicationUser(email=email, first_name='Admin', last_name='User', roles=[admin_role])
        user.set_password(password)
        user.save()

        # Inform the user
        #self.stdout.write(self.style.SUCCESS(f"Superuser '{uname}' with role '{role_name}' created successfully!"))