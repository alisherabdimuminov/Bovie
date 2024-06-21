from django.urls import path

from .views import (
    premieres,
    movie,
    most_recent,
    most_appearances,
    most_wanted,
    most_famous,
)


urlpatterns = [
    path("premieres/", premieres, name="premieres"),
    path("most_recent/", most_recent, name="most_recent"),
    path("most_appearances/", most_appearances, name="most_appearances"),
    path("most_wanted/", most_wanted, name="most_wanted"),
    path("most_famous/", most_famous, name="most_famous"),
    path("movie/<str:uid>/", movie, name="movie"),
]