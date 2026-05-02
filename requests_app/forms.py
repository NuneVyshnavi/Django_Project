from django import forms
from .models import FoodRequest

class FoodRequestForm(forms.ModelForm):
    class Meta:
        model = FoodRequest
        fields = [
            'ngo_name',
            'phone',
            'address'
        ]