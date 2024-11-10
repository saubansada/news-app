import datetime
from django.conf import settings
import jwt
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_mongoengine.serializers import DocumentSerializer
from apps.users.models import ApplicationUser, Role

class RoleSerizlizer(DocumentSerializer):
    class Meta:
        model = Role
        fields = ('name', 'description')
    
class ApplicationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationUser
        fields = '__all__'
        

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import ApplicationUser, Role

from rest_framework_simplejwt.tokens import RefreshToken

class CustomTokenObtainPairSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    @staticmethod
    def generate_tokens_for_user(user):
        
        # Define payload for access token
        access_payload = {
            'user_id': str(user.id),
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=15),  # Access token expiration
        }
        
        # Encode access token
        access_token = jwt.encode(access_payload, settings.SECRET_KEY, algorithm='HS256')

        # Define payload for refresh token
        refresh_payload = {
            'user_id': str(user.id),
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),  # Refresh token expiration
        }
        
        # Encode refresh token
        refresh_token = jwt.encode(refresh_payload, settings.SECRET_KEY, algorithm='HS256')

        return {
            'refresh': refresh_token,
            'access': access_token,
        }
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Authenticate the user based on email
        user = authenticate(request=self.context.get('request'), username=email, password=password)

        if not user:
            raise serializers.ValidationError('Invalid email or password')

        access_code = ""
        refresh_token = None

        try:
            refresh_token = CustomTokenObtainPairSerializer.generate_tokens_for_user(user)
            access_code = refresh_token['access']

            print("Access token: " + access_code)
        except Exception as e:
            print(e)

        return refresh_token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            return user
        raise serializers.ValidationError('Invalid credentials')