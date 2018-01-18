from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notification
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password','email', 'first_name', 'last_name', 'is_superuser', 'date_joined')

class NotificationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, required=False)
    class Meta:
        model = Notification
        fields = ('id',
                  'user',
                  'user_id',
                  'is_read',
                  'created_Date'
                  )
        read_only_fields = ['id']
