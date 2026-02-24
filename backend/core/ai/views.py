from django.shortcuts import render
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def chatbot(request):
    query = request.data.get("query")
    return Response({
        "reply": f"AI Response to: {query}",
        "agent": "academic-cluster"
    })
