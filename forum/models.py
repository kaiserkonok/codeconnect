from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('Q', 'Question'),
        ('A', 'Answer'),
    ]

    content_type = models.CharField(max_length=1, choices=CONTENT_TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent_post = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'

