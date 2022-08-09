from django.db import models
from django.contrib.auth import get_user_model
from .serializers import CommentSerializers
from .models import Comment


User = get_user_model()

class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    def __str__(self):
        return f"Comment{self.user.username} -> {self.post.title} [{self.created_at}]"


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    def __str__(self):
        return f"Like{self.user.username} -> {self.post.title} [{self.created_at}]"
        