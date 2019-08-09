from django.db import models
from django.contrib.auth.models import User
from mission.models import Mission

# Create your models here.
class Post(models.Model):
    writer = models.ForeignKey(User, related_name='writer', on_delete=models.CASCADE)
    mission_number = models.ForeignKey(Mission, related_name ='mission_num', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.ImageField(upload_to='images/')
    urlcontent = models.URLField(null=True,max_length=200)
    description = models.TextField()
    users = models.ManyToManyField(User, through='PostVote')

    def __str__(self):
        return self.title

class PostVote(models.Model):
    post = models.ForeignKey(Post, related_name='votelike', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='voteuser', on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        auto_now_add=True,
    )	