from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer
from .tasks import pushNotification

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    number = 1
    def createNotification(obj):
        for id in obj['user_ids']:
            notification = Notification()
            notification.user_id = id
            notification.message = obj['message']
            try:
                NotificationViewSet.perform_create(NotificationViewSet, notification)
            except Exception as e:
                print(e)
                return None
        # push bulk notification to certain users
        pushNotification(obj)
        return notification

    def perform_create(self, serializer):
        if(serializer):
            obj = serializer.save()
        return obj

