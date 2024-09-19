from django.db import models
from django.utils import timezone

class SongRequest(models.Model):
    artist_name = models.CharField(max_length=100)
    song_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.song_name} by {self.artist_name} (Requested by {self.user_name})"
