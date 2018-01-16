from django.shortcuts import render
from rest_framework import viewsets , serializers
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from redis import Redis
import json
from notification.views import NotificationViewSet
from notification.models import Notification
# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        result= User.objects.filter(username=request.data['username']) | User.objects.filter(email=request.data['email'])
        if(result):
            return Response("user cannot added", status=status.HTTP_400_BAD_REQUEST)
        print(request.data)
        print('hello from create')
        user = User.objects.create_user(request.data['username'], request.data['email'])
        notificationObj = {'user_id': 1, 'message': '', 'is_read': False}
        NotificationViewSet.createNotification(notificationObj)
        return Response("user created successfully", status=status.HTTP_200_OK)

