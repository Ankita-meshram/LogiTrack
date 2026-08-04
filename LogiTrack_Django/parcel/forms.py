from django import forms
from .models import Parcel


class ParcelForm(forms.ModelForm):

    class Meta:
        model = Parcel

        fields = [
            "sender_name",
            "sender_phone",
            "sender_address",
            "receiver_name",
            "receiver_phone",
            "receiver_address",
            "parcel_type",
            "weight",
        ]

        widgets = {

            "sender_name": forms.TextInput(attrs={
                "placeholder": "Sender Name"
            }),

            "sender_phone": forms.TextInput(attrs={
                "placeholder": "Sender Phone"
            }),

            "sender_address": forms.Textarea(attrs={
                "placeholder": "Sender Address"
            }),

            "receiver_name": forms.TextInput(attrs={
                "placeholder": "Receiver Name"
            }),

            "receiver_phone": forms.TextInput(attrs={
                "placeholder": "Receiver Phone"
            }),

            "receiver_address": forms.Textarea(attrs={
                "placeholder": "Receiver Address"
            }),

            "parcel_type": forms.TextInput(attrs={
                "placeholder": "Parcel Type"
            }),

            "weight": forms.NumberInput(attrs={
                "placeholder": "Weight (kg)"
            }),

        }