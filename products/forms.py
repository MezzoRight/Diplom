from django import forms
from django.forms import ModelForm, TextInput


class ProductSearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        label=False,
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control me-2', 'placeholder': 'Поиск'}
        )
    )