from django.db import models
import uuid
from shortuuid.django_fields import ShortUUIDField

from userauths.models import User

from core.constans import (
    ACCOUNT_STATUS,
    MARITAL_STATUS,
    GENDER,
    NATIONALITY_CHOICES,
    IDENTITY_TYPE
)


class Account(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(
        max_digits=12, decimal_places=2, default=0.00)
    account_number = ShortUUIDField(
        unique=True, length=10, max_length=25, prefix="217",
        alphabet="1234567890")
    account_id = ShortUUIDField(
        unique=True, length=7, max_length=25, prefix="PEX",
        alphabet="1234567890")
    pin_number = ShortUUIDField(
        unique=True, length=4, max_length=7, alphabet="1234567890")
    red_code = ShortUUIDField(unique=True, length=10,
                              max_length=10, alphabet="abcdefgh1234567890")
    account_status = models.CharField(
        max_length=100, choices=ACCOUNT_STATUS, default="in-active")
    date = models.DateTimeField(auto_now_add=True)
    kyc_submitted = models.BooleanField(default=False)
    kyc_confirmed = models.BooleanField(default=False)
    recommended_by = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, blank=True, null=True,
        related_name='recommended_by')

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return str(self.user)


class KYC(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account = models.OneToOneField(
        Account, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='kyc', default='default.jpg')
    marrital_status = models.CharField(choices=MARITAL_STATUS, max_length=40)
    gender = models.CharField(choices=GENDER, max_length=50)
    identity_type = models.CharField(choices=IDENTITY_TYPE, max_length=140)
    identity_image = models.ImageField(upload_to='kyc', null=True, blank=True)
    date_of_birth = models.DateTimeField(auto_now_add=False)
    signature = models.ImageField(upload_to='kyc')

    # Address
    country = models.CharField(
        choices=NATIONALITY_CHOICES, max_length=50, default='')
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    # contact Details
    mobile = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.user}"
