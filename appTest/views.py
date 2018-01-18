from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from notification.views import NotificationViewSet

# Create your views here.

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
        notificationObj = {'user_ids': [1, 4, 6], 'message': 'haaaaay from user '+user.username+' message from push notification queue ',
                           'broadcast': True}
        NotificationViewSet.createNotification(notificationObj)
        return Response("user created successfully", status=status.HTTP_200_OK)

