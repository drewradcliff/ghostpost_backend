from django.db import models
from django.utils import timezone


class Post(models.Model):
    is_boast = models.BooleanField()
    post_text = models.CharField(max_length=280)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    submission_date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(default=0)
