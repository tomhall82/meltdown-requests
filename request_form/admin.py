from django.contrib import admin
from .models import SongRequest

@admin.register(SongRequest)
class SongRequestAdmin(admin.ModelAdmin):
    list_display = ('song_name', 'artist_name', 'user_name', 'created_at')
    search_fields = ('song_name', 'artist_name', 'user_name')
