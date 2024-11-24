from django import forms
from .models import GeneralInfo

class GeneralInfoForm(forms.ModelForm):
    class Meta:
        model = GeneralInfo
        fields = ['name', 'phone_number', 'delivery_address', 'selected_plan', 'dietary_preference', 'Optional_Add_ons', 'token_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'delivery_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your delivery address', 'rows': 3}),
            'selected_plan': forms.Select(attrs={'class': 'form-control'}),
            'dietary_preference': forms.Select(attrs={'class': 'form-control'}),
            'Optional_Add_ons': forms.Textarea(attrs={'class': 'form-control'}),
        }
