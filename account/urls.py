from django.urls import path
from account import views

app_name = "account"

urlpatterns = [
    path("", views.account, name="account"),
    path("kyc-reg/", views.kyc_registration, name="kyc-reg"),
    path("kyc-update/", views.kyc_update, name="kyc-update"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
