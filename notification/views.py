from django.shortcuts import render
from rest_framework import viewsets, pagination
from .models import Notification
from .serializers import NotificationSerializer
# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def createNotification(obj):
        notification = Notification()
        notification.user_id = obj['user_id']
        notification.message = "test message for user"
        notification.is_read = obj['is_read']
        try:
            NotificationViewSet.perform_create(NotificationViewSet, notification)
        except Exception as e:
            print(e)
            return None
        return notification

    def perform_create(self, serializer):
        if(serializer):
            obj = serializer.save()
            NotificationViewSet.pushNotification(self, obj)
        return obj

    def pushNotification(self, obj):
        print('push Notification')