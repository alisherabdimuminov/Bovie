from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.admin import UserAdmin
from unfold.admin import ModelAdmin

from .forms import UserUpdateForm
from .models import User


@admin.register(User)
class UserModelAdmin(UserAdmin, admin.ModelAdmin):
    add_form = UserCreationForm
    form = UserUpdateForm
    add_fieldsets = (
        ("Foydalanuvchi qo'shish", {
            "fields": ("username", "password1", "password2", "first_name", "last_name",),
        }),
    )
    fieldsets = (
        ("Foydalanuvchini tahrirlash", {
            "fields": ("username", "first_name", "last_name", ),
        }),
    )
