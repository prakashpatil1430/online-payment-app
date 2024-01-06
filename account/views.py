from django.shortcuts import render, redirect, get_object_or_404
from account.models import KYC, Account, User
from account.forms import KYCForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cards.forms import CreditCardForm
from core.models import Notification
from cards.models import CreditCard
from transaction.models import Transaction


@login_required
def account(request):
    try:
        kyc = KYC.objects.get(user=request.user)
        account = Account.objects.get(user=request.user)
    except KYC.DoesNotExist:
        messages.warning(request, "You need to submit your KYC")
        return redirect("account:kyc-reg")
    except Account.DoesNotExist:
        messages.warning(request, "Account not found for the user")
        return redirect("core:index")

    context = {"kyc": kyc, "account": account}
    return render(request, "account/account.html", context)


@login_required
def kyc_registration(request):
    user = request.user
    account = Account.objects.get(user=user)

    try:
        user = request.user
        account = Account.objects.get(user=user)
        kyc = KYC.objects.get(user=user)
    except (User.DoesNotExist, account.DoesNotExist, KYC.DoesNotExist) as msg:
        kyc = None
        messages.warning(
            request, f"Error While submitting  KYC In review now {msg}.")
        return redirect("core:index")

    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(
                request, "KYC Form submitted successfully, In review now.")
            return redirect("core:index")
    else:
        form = KYCForm(instance=kyc)
    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }
    return render(request, "account/kyc-form.html", context)


@login_required
def kyc_update(request):
    user = request.user
    account = get_object_or_404(Account, user=user)
    kyc = get_object_or_404(KYC, user=user)

    if request.method == "POST":
        form = KYCForm(request.POST, request.FILES, instance=kyc)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = user
            new_form.account = account
            new_form.save()
            messages.success(
                request, "KYC Form submitted successfully, In review now.")
            return redirect("account:account")
    else:
        form = KYCForm(instance=kyc)

    context = {
        "account": account,
        "form": form,
        "kyc": kyc,
    }

    return render(request, "account/kyc-update.html", context)


@login_required
def dashboard(request):
    user = request.user
    try:
        kyc = KYC.objects.get(user=user)
    except KYC.DoesNotExist:
        messages.warning(request, "You need to submit your kyc")
        return redirect("account:kyc-reg")

    recent_transfer = Transaction.objects.filter(
        sender=user, transaction_type="transfer",
        status="completed").order_by("-id")[:1]

    recent_recieved_transfer = Transaction.objects.filter(
        reciever=user,
        transaction_type="transfer").order_by("-id")[:1]

    sender_transaction = Transaction.objects.filter(
        sender=user, transaction_type="transfer").order_by("-id")

    reciever_transaction = Transaction.objects.filter(
        reciever=user, transaction_type="transfer").order_by("-id")

    request_sender_transaction = Transaction.objects.filter(
        sender=user, transaction_type="request")

    request_reciever_transaction = Transaction.objects.filter(
        reciever=user, transaction_type="request")

    account = Account.objects.get(user=user)
    credit_cards = CreditCard.objects.filter(
        user=user).order_by("-id")

    if request.method == "POST":
        form = CreditCardForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()

            Notification.objects.create(
                user=request.user,
                notification_type="Added Credit Card"
            )

            messages.success(request, "Card Added Successfully.")
            return redirect("account:dashboard")
    else:
        form = CreditCardForm()

    context = {
        "kyc": kyc,
        "account": account,
        "form": form,
        "credit_card": credit_cards,
        "sender_transaction": sender_transaction,
        "reciever_transaction": reciever_transaction,
        'request_sender_transaction': request_sender_transaction,
        'request_reciever_transaction': request_reciever_transaction,
        'recent_transfer': recent_transfer,
        'recent_recieved_transfer': recent_recieved_transfer,
    }
    return render(request, "account/dashboard.html", context)
