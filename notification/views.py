from rest_framework import viewsets
from .models import Notification
from .serializers import NotificationSerializer
import redis
import json
from .redisConfig import RedisWrapper
# Create your views here.

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def createNotification(obj):
        for id in obj['user_ids']:
            notification = Notification()
            notification.user_id = id
            notification.message = obj['message']
            notification.is_read = False
            try:
                NotificationViewSet.perform_create(NotificationViewSet, notification)
            except Exception as e:
                print(e)
                return None
        NotificationViewSet.pushNotification(NotificationViewSet, obj)
        return notification

    def perform_create(self, serializer):
        if(serializer):
            obj = serializer.save()

        return obj

    def pushNotification(self, obj):
        response_data = {}
        response_data['msg'] = obj['message']
        response_data['toIds'] = obj['user_ids'],
        response_data['broadcast'] = 1 if obj['broadcast'] else 0
        print(response_data)
        try:
            r_server = RedisWrapper().redis_connect(server_key='local_server')
            r_server.ping()

            # r = redis.StrictRedis(host='localhost', port=6379, db=0)
            r_server.publish('notification', json.dumps(response_data))
        except Exception:
            print('cannot connect to redis server')
            print(Exception)