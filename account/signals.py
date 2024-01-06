# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from account.models import Account, KYC


@receiver(post_save, sender=User)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_account(sender, instance, **kwargs):
    instance.account.save()


@receiver(post_save, sender=KYC)
def update_kyc_submitted(sender, instance, created, **kwargs):
    if instance:
        instance.account.kyc_submitted = True
        instance.account.save()
