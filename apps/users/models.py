import datetime
from mongoengine import Document, StringField, ListField, ReferenceField, DateTimeField, BooleanField
from rest_framework import serializers, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

# 1. Role model: Define roles that users can have (like 'admin', 'user', etc.)
class Role(Document):
    name = StringField(required=True, unique=True)
    description = StringField()

    def __str__(self):
        return self.name
    

class ApplicationUser(Document):
    email = StringField(max_length=254, required=True, unique=True)
    phone_number = StringField(max_length=15, required=False, unique=True)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)
    roles = ListField(ReferenceField(Role))  # Many-to-many relationship with roles
    date_joined = DateTimeField(default=datetime.datetime.utcnow)
    is_active = BooleanField(default=True)
    password = StringField()

    def __str__(self):
        return self.email

    def set_password(self, password):
        """Hash the password (simple method for demonstration)."""
        from django.contrib.auth.hashers import make_password
        self.password = make_password(password)

    def check_password(self, password):
        """Check the password (simple method for demonstration)."""
        from django.contrib.auth.hashers import check_password
        return check_password(password, self.password)

    def has_role(self, role_name):
        """Check if the user has a specific role."""
        return any(role.name == role_name for role in self.roles)
    
    meta = {
        'collection': 'application_user'  # Name of the MongoDB collection
    }


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Custom logic for JWT authentication if needed
        return super().authenticate(request)
    
class HasRolePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user and user.has_role('admin'):  # Example: Check if user has 'admin' role
            return True
        return False