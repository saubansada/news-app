from rest_framework import viewsets, status, permissions
from .serializers import ApplicationUserSerializer, CustomTokenObtainPairSerializer
from apps.users.models import ApplicationUser
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Token view to get access and refresh tokens
class CustomTokenObtainPairView(TokenObtainPairView):
   serializer_class = CustomTokenObtainPairSerializer

class CustomTokenRefreshView(TokenRefreshView):
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = ApplicationUser.objects.all()
    serializer_class = ApplicationUserSerializer
    permission_classes = [permissions.AllowAny]  # Adjust permissions as needed

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Set password manually due to write_only field
        user.set_password(serializer.validated_data['password'])
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        queryset = super().get_queryset()
        role = self.request.query_params.get('role')
        if role:
            queryset = queryset.filter(roles__name=role)
        return queryset
    
 

# class AssignRoleViewSet(viewsets.ModelViewSet):
#     permission_classes = [permissions.IsAuthenticated, HasRolePermission]
#     required_role = 'admin'  # Set the required role for this view