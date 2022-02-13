from django.contrib import admin


from .models import IceCreamOrder


class IceCreamOrderAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'id', 'quantity')
    ordering = ('id',)


admin.site.register(IceCreamOrder, IceCreamOrderAdmin)
