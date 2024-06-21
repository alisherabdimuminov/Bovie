from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Genre, Movie, Comment


@admin.register(Genre)
class GenreModelAdmin(ModelAdmin):
    list_display = ["name"]


@admin.register(Movie)
class MovieModelAdmin(ModelAdmin):
    list_display = ["uid", "name", "author", "count_viewers", "rank", "search", "year", "length", "is_premiere"]


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    list_display = ["author", "movie", "comment", "created_at"]