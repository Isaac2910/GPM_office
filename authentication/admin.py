
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Rôle", {'fields': ('role',)}),
    )
    list_display = ('username', 'email','password', 'role', 'is_staff')

admin.site.register(User, UserAdmin)