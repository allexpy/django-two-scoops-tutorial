from django.contrib import admin


from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'scoops_ordered', 'store_visits')


admin.site.register(Customer, CustomerAdmin)
