
from django import forms

class Gform(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )
    roll_no = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )
    phone_no = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )
    email_id = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'input', 'placeholder': 'enter username'})
    )