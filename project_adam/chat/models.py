from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from users.models import User as User
# Create your models here.

'''class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=50)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile' '''

class ChatMessage(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From {self.user_from} to {self.user_to}: {self.message}"
