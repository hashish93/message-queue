from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notification(models.Model):
    message = models.CharField(max_length=1023)
    user = models.ForeignKey(User, null=False,blank=False, on_delete=models.CASCADE)
    created_Date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_read = models.BooleanField(default=False)
