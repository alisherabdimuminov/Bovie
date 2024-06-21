from django.urls import path

from .views import (
    premieres,
    movie,
    most_recent,
    most_appearances,
    most_wanted,
    most_famous,
    search,
    comment,
    feedback,
)

handler404 = "movies.views.handler404"

urlpatterns = [
    path("premieres/", premieres, name="premieres"), # premyeralar
    path("most_recent/", most_recent, name="most_recent"), # eng oxirgilari
    path("most_appearances/", most_appearances, name="most_appearances"), # eng ko'p ko'rilganlar
    path("most_wanted/", most_wanted, name="most_wanted"), # eng ko'p qidirilganlar
    path("most_famous/", most_famous, name="most_famous"), # eng mashxurlari
    path("movie/<str:uid>/", movie, name="movie"), # bitta kino
    path("search/<str:query>/", search, name="search"), # qidirish
    path("comment/", comment, name="comment"), # izox qoldirish
    path("feedback/", feedback, name="feedback"), # baho berish
]