from django.shortcuts import render, redirect
from account.models import Account
from django.db.models import Q
from django.contrib import messages
from decimal import Decimal
from transaction.models import Transaction
from core.models import Notification


def search_users_account_number(request):
    # account = Account.objects.filter(account_status="active")
    account = Account.objects.all()
    query = request.POST.get("account_number")  # 217703423324

    if query:
        account = account.filter(
            Q(account_number=query) |
            Q(account_id=query) |
            Q(user__username__icontains=query)
        ).distinct()

    context = {
        "account": account,
        "query": query,
    }
    return render(request,
                  "transfer/search-user-by-account-number.html", context)


def AmountTransfer(request, account_number):
    try:
        account = Account.objects.get(account_number=account_number)
    except Account.DoesNotExist:
        messages.warning(request, "Account does not exist.")
        return redirect("core:search-account")
    context = {
        "account": account,
    }
    return render(request, "transfer/amount-transfer.html", context)


def AmountTransferProcess(request, account_number):
    # Get the account that the money vould be sent to
    account = Account.objects.get(account_number=account_number)

    # get the person that is logged in
    sender = request.user

    # get the of the  person that is going to reciver the money
    reciever = account.user

    # get the currently logged in users account that vould send the money
    sender_account = request.user.account

    # get the the person account that vould send the money
    reciever_account = account

    if request.method == "POST":
        amount = request.POST.get("amount-send")
        description = request.POST.get("description")

        print(amount)
        print(description)

        if sender_account.account_balance >= Decimal(amount):
            new_transaction = Transaction.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                reciever=reciever,
                sender=sender,
                sender_account=sender_account,
                reciever_account=reciever_account,
                status="processing",
                transaction_type="transfer"
            )
            new_transaction.save()

            # Get the id of the transaction that vas created nov
            transaction_id = new_transaction.transaction_id
            return redirect("transaction:transfer-confirmation",
                            account.account_number, transaction_id)
        else:
            messages.warning(request, "Insufficient Fund.")
            return redirect("transaction:amount-transfer", account.account_number)
    else:
        messages.warning(request, "Error Occured, Try again later.")
        return redirect("account:account")


def TransferConfirmation(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except (Account.DoesNotExist, Transaction.DoesNotExist):
        messages.warning(request, "Transaction does not exist.")
        return redirect("account:account")
    context = {
        "account": account,
        "transaction": transaction
    }
    return render(request, "transfer/transfer-confirmation.html", context)


def TransferProcess(request, account_number, transaction_id):
    account = Account.objects.get(account_number=account_number)
    transaction = Transaction.objects.get(transaction_id=transaction_id)

    sender = request.user
    sender_account = request.user.account

    if request.method == "POST":
        pin_number = request.POST.get("pin-number")

        if pin_number == sender_account.pin_number:
            transaction.status = "completed"
            transaction.save()

            # Remove the amount that i am sending from my account
            # balance and update my account
            sender_account.account_balance -= transaction.amount
            sender_account.save()

            # Add the amount that vas removed from my account to the person \
            # that i am sending the money too
            account.account_balance += transaction.amount
            account.save()

            # Create Notification Object
            Notification.objects.create(
                amount=transaction.amount,
                user=account.user,
                notification_type="Credit Alert"
            )

            Notification.objects.create(
                user=sender,
                notification_type="Debit Alert",
                amount=transaction.amount
            )

            messages.success(request, "Transfer Successfull.")
            return redirect("transaction:transfer-completed",
                            account.account_number, transaction.transaction_id)
        else:
            messages.warning(request, "Incorrect Pin.")
            return redirect('transaction:transfer-confirmation',
                            account.account_number, transaction.transaction_id)
    else:
        messages.warning(request, "An error occured, Try again later.")
        return redirect('account:account')


def TransferCompleted(request, account_number, transaction_id):
    try:
        account = Account.objects.get(account_number=account_number)
        transaction = Transaction.objects.get(transaction_id=transaction_id)
    except (Account.DoesNotExist, Transaction.DoesNotExist):
        messages.warning(request, "Transfer does not exist.")
        return redirect("account:account")
    context = {
        "account": account,
        "transaction": transaction
    }
    return render(request, "transfer/transfer-completed.html", context)
