from django.db import models

# Create your models here.
class Mission(models.Model):
    mission_number = models.IntegerField()
    mission_name = models.CharField(max_length=200)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self):
        return self.mission_name