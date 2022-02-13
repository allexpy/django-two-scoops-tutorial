from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from .models import User


class MyUserAdmin(UserAdmin):
    model = User

    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('can_sprinkle',)}),
    )


admin.site.register(User, MyUserAdmin)
