from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UserProfileSerializer, PermissionSerializer, GroupSerializer
from django.contrib.auth.models import User, Permission, Group
from api_back.permissions import CustomDjangoModelPermissions
from api_back.pagination import CustomPagination


class GetUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['get']
    permission_classes = (CustomDjangoModelPermissions,)
    #pagination_class = CustomPagination


class PostUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['post']
    permission_classes = (CustomDjangoModelPermissions,)
    #pagination_class = CustomPagination


class PutUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['put']
    permission_classes = (CustomDjangoModelPermissions,)
    # pagination_class = CustomPagination


class DeleteUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    http_method_names = ['delete']
    #pagination_class = CustomPagination
    permission_classes = (CustomDjangoModelPermissions,)


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (CustomDjangoModelPermissions,)


# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#     pagination_class = CustomPagination
#     permission_classes = (CustomDjangoModelPermissions,)


class GetGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['get']
    # pagination_class = CustomPagination
    permission_classes = (CustomDjangoModelPermissions,)
    


class PostGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['post']
    #pagination_class = CustomPagination

    permission_classes = (CustomDjangoModelPermissions,)


class PutGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['put']
    #pagination_class = CustomPagination

    permission_classes = (CustomDjangoModelPermissions,)


class DeleteGroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    http_method_names = ['delete']
    #pagination_class = CustomPagination

    permission_classes = (CustomDjangoModelPermissions,)

