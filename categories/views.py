from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
# Create your views here.
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework import status

class CategoryListView(APIView):
    model = Category

    def get(self, request):
        categoris = Category.objects.filter(user_id= request.user)  # filter by user
        serilaizer = CategorySerializer(categoris, many=True)
        return Response({
            "data":[]            
         },
            status=status.HTTP_200_OK
        )
