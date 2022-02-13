from django.contrib import admin


from .models import FlavorReview


class FlavorReviewAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'id', 'pub_date')
    ordering = ('id',)

admin.site.register(FlavorReview, FlavorReviewAdmin)
