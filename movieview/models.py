from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=30)
    shot_desc = models.CharField(max_length=350)
    long_desc = models.CharField(max_length=600)
    thumbnail = models.CharField(max_length=500)
    video_url = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    @staticmethod
    def get_name():
        return 'movies'
