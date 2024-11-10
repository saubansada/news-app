from django.contrib.auth.backends import BaseBackend
from .models import ApplicationUser

class EmailAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Find the user by email
            user = ApplicationUser.objects.get(email=username)
            # Check if password is correct
            if user.check_password(password):
                return user
        except Exception as ex:
            print(ex)
            return None
        return None