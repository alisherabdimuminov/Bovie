from uuid import uuid4
from django.db import models
from users.models import User

from .utils import max_value_validator, min_value_validator, truncate


class Genre(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Janr nomi")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"
    

class Movie(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Kino nomi")
    uid = models.UUIDField(verbose_name="ID", editable=False, default=uuid4)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Kino muallifi")
    genre = models.ManyToManyField(Genre, related_name="movie_genres", verbose_name="Kino janrlari")
    trailer = models.FileField(upload_to="trailers", verbose_name="Kino trayleri")
    banner = models.ImageField(upload_to="banners", verbose_name="Kino banneri")
    description = models.TextField(verbose_name="Kino haqida qisqacha")
    year = models.CharField(max_length=10, verbose_name="Kino yili")
    source = models.FileField(upload_to="movies", verbose_name="Kino")
    rank = models.DecimalField(max_digits=5, decimal_places=1, validators=[min_value_validator, max_value_validator])
    viewers = models.ManyToManyField(User, related_name="movie_viewers", null=True, blank=True, verbose_name="Kinoni tomosha qilganlar")
    feedbackers = models.ManyToManyField(User, related_name="movei_feedbackers", null=True, blank=True, verbose_name="Kinoga baho berganlar")
    feedback = models.DecimalField(default=0, null=True, blank=True, decimal_places=1, max_digits=10)
    search = models.IntegerField(default=0, verbose_name="Kino qidiruvlar soni")
    price = models.IntegerField(verbose_name="Kino narxi", default=0)
    is_premiere = models.BooleanField(default=False, verbose_name="Kino premyerami?")
    length = models.IntegerField(verbose_name="Kino davomiyligi")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def count_viewers(self):
        return self.viewers.all().count()
    
    def comments(self):
        return Comment.objects.filter(movie=self)
    
    def count_comments(self):
        return Comment.objects.filter(movie=self).count()
    
    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Izox maullifi")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Kino")
    body = models.TextField(verbose_name="Izox matni")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def comment(self):
        return truncate(self.body)

    class Meta:
        verbose_name = "Izox"
        verbose_name_plural = "Izoxlar"

