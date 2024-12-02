from django.contrib import admin
from .models import Game, Genre

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'vote_average', 'popularity')
    search_fields = ('title', 'description')
    list_filter = ('release_date', 'genres')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
