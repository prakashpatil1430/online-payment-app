from django.contrib import admin

from cards.models import (
    CreditCard,
)


class CreditCardAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'card_type']
    list_display = ['user', 'amount', 'card_type']


admin.site.register(CreditCard, CreditCardAdmin)
