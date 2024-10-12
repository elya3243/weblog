from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    produce = models.DateTimeField(auto_now_add=True)
    auther = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
