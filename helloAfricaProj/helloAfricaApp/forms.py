# forms.py
from django import forms
from .models import ContactMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
