from django.urls import path

from .views import (
    card_detail,
    fund_credit_card,
    withdraw_fund,
    delete_card
)
app_name = 'cards'

urlpatterns = [
    #     # Credit Card URLS
    path("card/<card_id>/", card_detail, name="card-detail"),
    path("fund-credit-card/<card_id>/",
         fund_credit_card, name="fund-credit-card"),
    path("withdraw_fund/<card_id>/",
         withdraw_fund, name="withdraw_fund"),
    path("delete_card/<card_id>/", delete_card, name="delete_card")
]
