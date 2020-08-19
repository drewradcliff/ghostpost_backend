from django.db import models


class Post(models.Model):
    is_boast = models.BooleanField()
    post_text = models.CharField(max_length=280)
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()
    submission_date = models.DateTimeField(auto_now=False, auto_now_add=False)
