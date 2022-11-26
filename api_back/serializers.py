from email.policy import default
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from django.contrib.auth.models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from rest_framework.authtoken.models import Token


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    permissions_list = PermissionSerializer(source="permissions", many=True, read_only=True)
    class Meta:
        model = Group
        fields = ('pk', 'id', 'name', 'permissions_list')

class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    group = serializers.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('id', 'username', 'password1','password2', 'email', 'first_name', 'last_name', 'group')

    # override get_cleaned_data of RegisterSerializer
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name'),
            'last_name': self.validated_data.get('last_name'),
        }

    # override save method of RegisterSerializer
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        group = self.validated_data.get('group')
        group_id = Group.objects.get(pk=group)
        user.save()
        user.groups.add(group_id.pk)
        Token.objects.create(user=user)
        adapter.save_user(request, user, self)
        return user
    
        
class UserProfileSerializer(serializers.ModelSerializer):  
    groups_list = GroupSerializer(source="groups", many=True, read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'password')
    