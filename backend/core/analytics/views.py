from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def dashboard(request):
    return Response({
        "users": 1200,
        "students": 900,
        "faculty": 80,
        "branches": 5
    })
