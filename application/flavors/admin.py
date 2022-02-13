from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Flavor


class FlavorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'scoops_remaining', 'slug', 'created', 'modified')
    ordering = ('id',)


admin.site.register(Flavor, FlavorAdmin)
