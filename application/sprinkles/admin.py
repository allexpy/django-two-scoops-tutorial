from django.contrib import admin


from .models import Sprinkles


class SprinklesAdmin(admin.ModelAdmin):
    list_display = ('name', 'labels', 'price', 'id')





admin.site.register(Sprinkles, SprinklesAdmin)
