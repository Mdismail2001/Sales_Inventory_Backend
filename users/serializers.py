from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email', 'password', 'mobile']
    
    
    def create(self, validated_data):
        
        user = User.objects.create_user(**validated_data)
        return user

    
    # system 1 
    # user = user (
    #     firsName = validated_data['firstName'],
    #     lastName = validated_data['lastName'],
    #     email = validated_data['email'],
    #     mobile = validated_data['mobile'],
    # )
    # user.set_password(validated_data['password'])
    # user.save()
    # return user
    
    # # system 2
    # user = User.objects.create_user(
    #     firstName = validated_data['firstName'],
    #     lastName = validated_data['lastName'],
    #     email = validated_data['email'],
    #     mobile = validated_data['mobile'],
    #     password = validated_data['password'],  
    # )
    
    
