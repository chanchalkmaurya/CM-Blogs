from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title[:11] 