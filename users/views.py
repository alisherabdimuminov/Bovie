from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from .models import User


@api_view(http_method_names=["POST"])
def login(request: HttpRequest):
    username: str = request.data.get("username")
    password: str = request.data.get("password")
    if not username:
        return Response({
            "status": "error",
            "errors": {
                "username": "username bo'sh bo'lmasligi kerak"
            },
            "data": {}
        })
    if not password:
        return Response({
            "status": "error",
            "errors": {
                "password": "password bo'sh bo'lmasligi kerak"
            }
        })
    user: User | None = authenticate(request=request, username=username, password=password)
    if not user:
        return Response({
            "status": "error",
            "errors": {
                "user": "Foydalanuvchi topilmadi yoki parolni to'g'ri kiriting"
            }
        })
    token:Token | None = Token.objects.get_or_create(user=user)
    if not token:
        return Response({
            "status": "error",
            "errors": {
                "token": "Token mavjud emas"
            }
        })
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "token": token.key,
        }
    })


@api_view(http_method_names=["POST"])
def signup(request: HttpRequest):
    username: str | None = request.data.get("username")
    first_name: str | None = request.data.get("first_name")
    last_name: str | None = request.data.get("last_name")
    password: str | None = request.data.get("password")
    if not username:
        return Response({
            "status": "error",
            "errors": {
                "username": "username bo'sh bo'lishi mumkin emas"
            },
            "data": {}
        })
    if not first_name:
        return Response({
            "status": "error",
            "errors": {
                "first_name": "first_name bo'sh bo'lishi mumkin emas"
            },
            "data": {}
        })
    if not last_name:
        return Response({
            "status": "error",
            "errors": {
                "last_name": "last_name bo'sh bo'lishi mumkin emas"
            },
            "data": {}
        })
    if not password:
        return Response({
            "status": "error",
            "errors": {
                "password": "password bo'sh bo'lishi mumkin emas"
            },
            "data": {}
        })
    user = User.objects.filter(username=username)
    if user:
        return Response({
            "status": "error",
            "errors": {
                "username": "Bu telefon raqami oldin ro'yxatdan o'tgan"
            },
            "data": {}
        })
    user = User.objects.create(
        username=username,
        first_name=first_name,
        last_name=last_name,
    )
    user.set_password(raw_password=password)
    user.save()
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "message": "Muvaffaqiyatli ro'yxatdan o'tdingiz"
        }
    })
