from django.urls import path

from .views import (
    transaction_detail,
    transaction_lists
)
from . import payment_request
from .payment_transfer import (search_users_account_number,
                               AmountTransfer,
                               AmountTransferProcess,
                               TransferConfirmation,
                               TransferProcess,
                               TransferCompleted,
                               )


app_name = "transaction"

urlpatterns = [

    # transfer
    path('search_account/', search_users_account_number,
         name='search-account'),
    path("amount-transfer/<account_number>/",
         AmountTransfer, name="amount-transfer"),
    path("amount-transfer-process/<account_number>/",
         AmountTransferProcess, name="amount-transfer-process"),
    path("transfer-confirmation/<account_number>/<transaction_id>/",
         TransferConfirmation, name="transfer-confirmation"),
    path("transfer-process/<account_number>/<transaction_id>/",
         TransferProcess, name="transfer-process"),
    path("transfer-completed/<account_number>/<transaction_id>/",
         TransferCompleted, name="transfer-completed"),


    # transactions
    path("transactions/", transaction_lists, name="transactions"),
    path("transaction-detail/<transaction_id>/",
         transaction_detail, name="transaction-detail"),

    # Payment Request
    path("request-search-account/", payment_request.SearchUsersRequest,
         name="request-search-account"),
    path("amount-request/<account_number>/",
         payment_request.AmountRequest, name="amount-request"),
    path("amount-request-process/<account_number>/",
         payment_request.AmountRequestProcess, name="amount-request-process"),
    path("amount-request-confirmation/<account_number>/<transaction_id>/",
         payment_request.AmountRequestConfirmation,
         name="amount-request-confirmation"),
    path("amount-request-final-process/<account_number>/<transaction_id>/",
         payment_request.AmountRequestFinalProcess,
         name="amount-request-final-process"),
    path("amount-request-completed/<account_number>/<transaction_id>/",
         payment_request.RequestCompleted, name="amount-request-completed"),

    # Request Settlement
    path("settlement-confirmation/<account_number>/<transaction_id>/",
         payment_request.settlement_confirmation,
         name="settlement-confirmation"),
    path("settlement-processing/<account_number>/<transaction_id>/",
         payment_request.settlement_processing, name="settlement-processing"),
    path("settlement-completed/<account_number>/<transaction_id>/",
         payment_request.SettlementCompleted, name="settlement-completed"),
    path("delete-request/<transaction_id>/",
         payment_request.deletepaymentrequest, name="delete-request"),


]
