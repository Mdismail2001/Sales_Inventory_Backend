from django.shortcuts import render
from rest_framework.views import APIView
from .models import Category
# Create your views here.
from rest_framework.response import Response
from .serializers import CategorySerializer
from rest_framework import status
from rest_framework import permissions

class CategoryListView(APIView):
    parser_classes = [permissions.IsAuthenticated]

    def get(self, request):
        categoris = Category.objects.filter(user_id= request.user)  # filter by user
        serilaizer = CategorySerializer(categoris, many=True)
        
        if categoris.exists():
            return Response(
                {
                    "status": "success",
                    "message": "Data Found",
                    "data" : serilaizer.data
                }, status=status.HTTP_200_OK
            )

        return Response(
            {
                "status": "success",
                "message": "Data Not Found",
                "data": []
            }, status=status.HTTP_200_OK
        )





class CategoryCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


class CategoryUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request,):
        cate_id = request.data.get('id')
        
        try:
            category = Category.objects.get(id=cate_id, user_id = request.user.id)
            serializer = CategorySerializer(category, data=request.data)
                    
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Category.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Category not found"
            }, status=status.HTTP_404_NOT_FOUND
            )



class CategoryDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request,pk):
        
        try:
            category = Category.objects.get(id=pk, user_id=request.user.id)
            category.delete()
            return Response({
                "status": "success",
                "message": "Category deleted successfully"
            }, status=status.HTTP_200_OK
            )
        except Category.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Category not found"
            }, status=status.HTTP_404_NOT_FOUND
            )