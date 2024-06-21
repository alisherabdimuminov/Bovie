from rest_framework.serializers import ModelSerializer

from .models import Movie, Genre, Comment
from users.models import User


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", )

class GenreModelSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ("name", )


class CommentModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(User, many=False)
    class Meta:
        model = Comment
        fields = ("author", "id", "body", "created_at", )


class MoviesModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(User, many=False)
    class Meta:
        model = Movie
        fields = ("name", "uid", "author", "banner", "length", "rank", "count_viewers", )


class MovieModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(User, many=False)
    genre = GenreModelSerializer(Genre, many=True)
    comments = CommentModelSerializer(Comment, many=True)
    class Meta:
        model = Movie
        fields = ("name", "uid", "author", "genre", "year", "description", "price", "is_premiere", "banner", "trailer", "rank", "source", "length", "count_viewers", "comments", )
