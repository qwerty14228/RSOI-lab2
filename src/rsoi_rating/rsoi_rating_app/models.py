from django.db import models

class Rating(models.Model):
    username = models.CharField(max_length=80)
    stars = models.IntegerField(min=0, max=100)