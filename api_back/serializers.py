from email.policy import default
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from django.db import models



class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    permissions_list = PermissionSerializer(source="permissions", many=True, read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'permissions_list',)

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()
    class Meta:
        model = User
        fields = '__all__'

    # override get_cleaned_data of RegisterSerializer
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name'),
            'last_name': self.validated_data.get('last_name'),
            'is_staff': self.validated_data.get('is_staff'),
            'is_superuser': self.validated_data.get('is_superuser'),
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()
        adapter.save_user(request, user, self)
        user.is_active = True
        return user
    
        
class UserProfileSerializer(serializers.ModelSerializer):  
    groups_list = GroupSerializer(source="groups", many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'password')
    