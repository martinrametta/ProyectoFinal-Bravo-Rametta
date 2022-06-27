from django.db import models
from django.contrib.auth.models import User


class Messages(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver")
    msg = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return f"{self.msg[:50]}[...]"

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)   #vinvulo con el usuario
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)  #Subcaperta avatars de media

    def __str__(self):
        return f"Profile image from user: {self.user.username}"



