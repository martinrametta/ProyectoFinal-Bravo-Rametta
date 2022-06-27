from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', null=True, blank = True)
    content = RichTextField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title
