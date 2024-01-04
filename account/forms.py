from django import forms
from account.models import KYC
from django.forms import ImageField, FileInput
from core.models import CreditCard


class DateInput(forms.DateInput):
    input_type = 'date'


class KYCForm(forms.ModelForm):
    identity_image = ImageField(widget=FileInput)
    image = ImageField(widget=FileInput)
    signature = ImageField(widget=FileInput)

    class Meta:
        model = KYC
        fields = ['full_name', 'image', 'marrital_status', 'gender',
                  'identity_type', 'identity_image', 'date_of_birth',
                  'signature', 'country', 'state', 'city', 'mobile', 'fax']
        widgets = {
            "full_name": forms.TextInput(attrs={"placeholder": "Full Name"}),
            "mobile": forms.TextInput(attrs={"placeholder": "Mobile Number"}),
            "fax": forms.TextInput(attrs={"placeholder": "Fax Number"}),
            "country": forms.TextInput(attrs={"placeholder": "Country"}),
            "state": forms.TextInput(attrs={"placeholder": "State"}),
            "city": forms.TextInput(attrs={"placeholder": "City"}),
            'date_of_birth': DateInput
        }


class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Card Holder Name"}))
    number = forms.IntegerField(widget=forms.NumberInput(
        attrs={"placeholder": "Card Number"}))
    month = forms.IntegerField(widget=forms.NumberInput(
        attrs={"placeholder": "Expiry Month"}))
    year = forms.IntegerField(widget=forms.NumberInput(
        attrs={"placeholder": "Expiry Month"}))
    cvv = forms.IntegerField(
        widget=forms.NumberInput(attrs={"placeholder": "CVV"}))

    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'month', 'year', 'cvv', 'card_type']
