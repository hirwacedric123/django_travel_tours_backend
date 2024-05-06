# forms.py
from django import forms
from .models import ContactMessage, BookingMessage

class MessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message']
class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingMessage
        fields =['username','useremail', 'telnumber','destination', 'howMany', 'arrivals',  'bookmessage']

