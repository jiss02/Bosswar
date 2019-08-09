from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    # email = models.EmailField(null=True) 
    
    phonenumber = models.CharField(
        max_length=13,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"\d{3}-\d{3,4}-\d{4}",
                message='010-1234-5678 형식으로 입력하세요.',
            )
        ]
    )
    point = models.IntegerField(default=500)
    votes = models.IntegerField(default=2)

    def __str__(self):
        return self.phonenumber