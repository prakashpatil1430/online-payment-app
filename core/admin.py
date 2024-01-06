from django.contrib import admin

from core.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user', 'notification_type', 'amount', 'date']


admin.site.register(Notification, NotificationAdmin)
