from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notification
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'password','email', 'first_name', 'last_name', 'is_superuser', 'date_joined')

class NotificationSerializer(serializers.Serializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='user',
                                                          allow_null=False, required=True)
    message = serializers.CharField(max_length=1023)
    created_Date = serializers.DateTimeField()
    is_read = serializers.BooleanField(default=False)
    class Meta:
        model = Notification
        fields = ('id'
                  'user_id',
                  'is_read',
                  'created_Date'
                  )
        read_only_fields = ['id']
