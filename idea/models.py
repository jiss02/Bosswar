from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Idea(models.Model):
    whoseidea =  models.ForeignKey(User, related_name='whoseidea', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Ideacomment(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE)
    comment = models.CharField(max_length=800)