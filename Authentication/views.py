from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
