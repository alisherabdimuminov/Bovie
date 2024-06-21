from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Genre, Movie, Comment


@admin.register(Genre)
class GenreModelAdmin(ModelAdmin):
    list_display = ["name"]


@admin.register(Movie)
class MovieModelAdmin(ModelAdmin):
    list_display = ["name", "author"]


@admin.register(Comment)
class CommentModelAdmin(ModelAdmin):
    list_display = ["author", "movie", "created_at"]