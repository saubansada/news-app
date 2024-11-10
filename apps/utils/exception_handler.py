from django.forms import ValidationError
from django.http import Http404, JsonResponse
from rest_framework.views import exception_handler, PermissionDenied
from rest_framework.response import Response
from rest_framework import status
from exception_handler import InvalidURLException


def custom_exception_handler(exc, context):
    # Log the exception for debugging 

    # Customize error response based on exception type
    if isinstance(exc, Http404):
        return JsonResponse({'detail': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    elif isinstance(exc, PermissionDenied):
        return JsonResponse({'detail': 'Permission Denied'}, status=status.HTTP_403_FORBIDDEN)
    elif isinstance(exc, ValidationError):
        return JsonResponse({'detail': exc.messages}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # Return a generic 500 error response
        return JsonResponse({'detail': 'Server Error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
def custom_exception_handler2(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 403:
        response.data = {
            "detail": "You do not have permission to perform this action.",
            "status_code": 403
        }
    elif response is None:
        response = Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED
        )
    return response