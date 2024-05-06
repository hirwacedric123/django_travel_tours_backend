from django.db import models

# Create your models here.
# models.py
from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class BookingMessage(models.Model):
    username=models.CharField(max_length=100)
    useremail = models.EmailField()
    telnumber=models.CharField(max_length=16)
    destination=models.CharField(max_length=50)
    howMany=models.CharField(max_length=10)
    arrivals=models.DateTimeField()
    bookmessage=models.TextField()

