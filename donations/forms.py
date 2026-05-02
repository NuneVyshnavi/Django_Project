from django import forms
from .models import Donation 

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = [
            'food_name',
            'category',
            'quantity',
            'description',
            'expiry_time',
            'image'
        ]
        widgets={
            'expiry_time':forms.DateTimeInput(
                attrs={
                    'type':'datetime-local'
                }
            )
        }