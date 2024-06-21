from django.http import HttpRequest
from django.db.models import Count
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import Genre, Movie, Comment
from .serializers import (
    MoviesModelSerializer,
    MovieModelSerializer,
)


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def premieres(request: HttpRequest):
    movies_obj = Movie.objects.filter(is_premiere=True).order_by('-id')
    movies = MoviesModelSerializer(movies_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "movies": movies.data
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def most_recent(request: HttpRequest):
    movies_obj = Movie.objects.order_by("-id")
    movies = MoviesModelSerializer(movies_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "movies": movies.data
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def most_famous(request: HttpRequest):
    movies_obj = Movie.objects.order_by("-rank")
    movies = MoviesModelSerializer(movies_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "movies": movies.data
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def most_appearances(request: HttpRequest):
    movies_obj = Movie.objects.annotate(num_viewers=Count("viewers")).order_by("-num_viewers")
    movies = MoviesModelSerializer(movies_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "movies": movies.data,
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def most_wanted(request: HttpRequest):
    movies_obj = Movie.objects.order_by("-search")
    movies = MoviesModelSerializer(movies_obj, many=True)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "movies": movies.data
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def movie(request: HttpRequest, uid: str):
    movie_obj = get_object_or_404(Movie, uid=uid)
    movie = MovieModelSerializer(movie_obj, many=False)
    # movie_obj.viewers.add(request.user)
    # movie_obj.save()
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "movie": movie.data,
        }
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def comment(request: HttpRequest):
    movie_id: str | None = request.data.get("movie_id")
    body: str = request.data.get("body")
    movie = get_object_or_404(Movie, uid=movie_id)
    if not movie_id:
        return Response({
            "status": "error",
            "errors": {
                "movie_id": "movie_id to'ldirilishi shart.",
            },
            "data": {},
        })
    if not body:
        return Response({
            "status": "error",
            "errors": {
                "body": "body to'ldirilishi shart.",
            },
        })
    comment = Comment.objects.create(
        author=request.user,
        movie=movie,
        body=body
    )
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "message": "Izox qoldirish muvaffaqiyatli amalga oshirildi."
        },
    })


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[TokenAuthentication])
@permission_classes(permission_classes=[IsAuthenticated])
def feedback(request: HttpRequest):
    movie_id: str | None = request.data.get("movie_id")
    feed: str | None = request.data.get("feedback")
    if not movie_id:
        return Response({
            "status": "success",
            "errors": {
                "movie_id": "movie_id to'ldirilishi shart"
            },
            "data": {},
        })
    if not feed:
        return Response({
            "status": "success",
            "errors": {
                "feedback": "feedback to'ldirilishi shart.",
            },
            "data": {},
        })
    movie = get_object_or_404(Movie, uid=movie_id)
    movie_rank = movie.rank
    feedbackers = movie.feedbackers.count()
    feedback_obj = (movie_rank + float(feed)) / (feedbackers + 1)
    movie.rank = feedback_obj
    movie.save()
    return Response({
        "status": "success",
        "errors": {},
        "data": {}
    })