from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({
                "status": "success", 
                "message": "User Registration Successfully"
                },status=status.HTTP_201_CREATED)

        return Response({
            "status": "error",
            "message": "User Registration Failed",
        }, status=status.HTTP_400_BAD_REQUEST)
