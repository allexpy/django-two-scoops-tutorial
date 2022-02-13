from django.contrib import admin


from .models import Voucher


class VoucherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'birth_date')


admin.site.register(Voucher, VoucherAdmin)
