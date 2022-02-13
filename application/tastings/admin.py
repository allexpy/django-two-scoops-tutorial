from django.contrib import admin


from .models import Taster, Tasting


class TasterAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TastingAdmin(admin.ModelAdmin):
    list_display = ('taster', 'tasted_flavor', 'opinion', 'id')


admin.site.register(Taster, TasterAdmin)
admin.site.register(Tasting, TastingAdmin)
