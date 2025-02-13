from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status
# for login
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# for send otp
from django.contrib.auth import get_user_model
import random
from django.core.mail import send_mail
# for reset password
from rest_framework import permissions
# user profile
# from rest_framework.permissions import IsAuthenticated


User = get_user_model()



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
        
        
        
        
class UserLoginView(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                "status": "success",
                "message": "User Login Successfully",
                "token": str(refresh.access_token)
                },
                status=status.HTTP_200_OK
                )
        return Response(
            {
            "status": "Unauthorized",
            "message": "User Login Failed",
            },
            status=status.HTTP_400_BAD_REQUEST
        )




class SendOtpViews(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email or not User.objects.filter(email=email).exists():
            return Response({
                "status": "failed",
                "message": "valid email is required"
            })
        
        otp = str(random.randint(100000, 999999))
        user = User.objects.get(email=email)
        user.otp = otp
        user.save()
        
        send_mail(
            subject="OTP For Password Reset",
            message=f"Your OTP is {otp}",
            from_email="OTP Sales Inventory<salesinventory@gmail.com>",
            recipient_list=[email],
        )
        
        return Response({
            "status": "success",
            "message": "OTP send successfully"},
            status=status.HTTP_200_OK
        )
 
 
 
class VarifyOtpViwes(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if not email or not otp:
            return Response({
                "status": "failed",
                "message": "valid email and otp are required"},
                status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(email=email, otp=otp)
            # user.otp = None
            user.save() 
            token =str( RefreshToken.for_user(user).access_token)
            return Response({
                "status": "success",
                "message": "OTP varified successfully",
                "token": token},
                status=status.HTTP_200_OK)
            
        except User.DoesNotExist:
            return Response({
                "status": "failed",
                "message": "Invalid OTP"},
                status=status.HTTP_400_BAD_REQUEST)
        




class ResetPasswordViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        password = request.data.get('password')
        
        if not password:
            return Response({
                "status": "failed",
                "message": "valid password is required"},
                status=status.HTTP_400_BAD_REQUEST)
        
        user = request.user
        user.set_password(password)
        user.save()
        return Response({
            "status":"success",
            "message":"Password Reset Successfully"
        })



class UserProfileViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user_data = UserProfileSerializer(user).data
        return Response(
            {"status": "success",
             "message": "Request Successfull",
             "data": user_data
             },
            status=status.HTTP_200_OK
            )
    
    
class UpdateUserProfileViews(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        user = request.user
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response({
                "status": "Success",
                "message": "User Profile Update Successfuly"
                },
                status=status.HTTP_200_OK
            )
        
        return Response({
            "status": "Failed",
            "message": "User Profile Update Failed"
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
        