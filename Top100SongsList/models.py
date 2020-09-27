from django.db import models


class Hot100Data(models.Model):

    rank = models.BigIntegerField()
    song_name = models.CharField(max_length=50)
    artists = models.CharField(max_length=50)
    peak_rank = models.BigIntegerField()
    weeks_on_chart = models.BigIntegerField()
    rank_last_week = models.BigIntegerField()
    
    def __str__(self):
        return self.song_name