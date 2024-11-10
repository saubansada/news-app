from django.http import Http404, JsonResponse
from rest_framework.views import exception_handler, PermissionDenied, status
from rest_framework.response import Response

class CustomExceptionMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
         
        # if request.path.startswith('/api/')  and (request.user is None or not request.user.is_authenticated):
        #     return JsonResponse({'detail': 'Unauthorized access'}, status=401)

        # Customize error handling based on exception type
        if isinstance(exception, Http404):
            return JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        elif isinstance(exception, PermissionDenied):
            return JsonResponse({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)
        
        # Use DRF's exception handler to get the initial response
        response = exception_handler(exception, context={'request': request})

        # Check if response is None (unhandled exception)
        if response is None:
            # Handle as a server error if not handled by DRF's exception handler
            return JsonResponse(
                {
                    'error': 'Server Error',
                    'detail': str(exception)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
        # Modify the response data if it exists
        response.data = {
            'error': 'Server Error',
            'detail': str(exception)
        }

        # Return a JsonResponse with the status from the original response
        return JsonResponse(response.data, status=response.status_code)
 

        