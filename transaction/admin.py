from django.contrib import admin

from transaction.models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type']
    list_display = ['user', 'amount', 'status',
                    'transaction_type', 'reciever', 'sender', 'date']


admin.site.register(Transaction, TransactionAdmin)
