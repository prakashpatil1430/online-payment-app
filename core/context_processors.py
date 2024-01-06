# core/context_processors.py

from core.models import Notification


# def notifications(request):
#     try:
#         notifications = Notification.objects.filter(
#             user=request.user).order_by("-id")[:10]
#     except Notification.DoesNotExist:
#         pass

#     return {
#         "notifications": notifications,
#     }


def notifications(request):
    if request.user.is_authenticated:
        notifications = Notification.objects.filter(
            user=request.user).order_by("-id")[:10]
    else:
        notifications = None
    return {
        "notifications": notifications,
    }
