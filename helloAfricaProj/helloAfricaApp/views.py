from django.core.mail import send_mail
from mailbox import Message
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from .forms import MessageForm, BookingForm
import logging



def index(request):
    return render(request, 'index.html')

def contact(request):
    return render (request, 'contact.html')
def safarisDetails(request):
    return render (request, 'safaris-details.html')
def book_page(request):
    return render (request, 'book.html')
def terms_and_conditions(request):
    return render (request, 'terms-and-conditions.html')

# View function for sending message
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_instance = form.save()

            # Send email notification to admin
            admin_subject = 'New message from {}'.format(message_instance.name)
            admin_message = render_to_string('email/admin_notification_template.html', {
                'name': message_instance.name,
                'email': message_instance.email,
                'phone': message_instance.phone,
                'message': message_instance.message
            })
            admin_email = 'hirwacedric123@gmail.com'
            admin_email_text = strip_tags(admin_message)
            admin_email_html = admin_message
            admin_email = EmailMultiAlternatives(admin_subject, admin_email_text, 'hirwacedric123@gmail.com', [admin_email])
            admin_email.attach_alternative(admin_email_html, "text/html")
            admin_email.send()

            # Send email confirmation to user
            user_subject = 'Message Confirmation'
            user_message = render_to_string('email/user_notification_template.html', {
                'name': message_instance.name,
                'email': message_instance.email,
                'phone': message_instance.phone,
                'message': message_instance.message,
            })
            user_email_text = strip_tags(user_message)
            user_email_html = user_message
            user_email = EmailMultiAlternatives(user_subject, user_email_text, 'hirwacedric123@gmail.com', [message_instance.email])
            user_email.attach_alternative(user_email_html, "text/html")
            user_email.send()

            return render(request, 'contact.html')  # Redirect to success page

    else:
        form = MessageForm()

    return render(request, 'index.html', {'form': form})



logger = logging.getLogger(__name__)

# View function for handling bookings
def books(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save()

            # Send email notification to admin
            try:
                admin_subject = 'New booking from {}'.format(booking_instance.username)
                admin_message = render_to_string('email/admin_notification_template.html', {
                    'username': booking_instance.username,
                    'useremail': booking_instance.useremail,
                    'telnumber': booking_instance.telnumber,
                    'destination': booking_instance.destination,
                    'howMany': booking_instance.howMany,
                    'arrivals': booking_instance.arrivals,
                    'bookmessage': booking_instance.bookmessage,
                })
                admin_email_text = strip_tags(admin_message)
                admin_email_html = admin_message
                admin_email = EmailMultiAlternatives(admin_subject, admin_email_text, 'hirwacedric123@gmail.com', ['hirwacedric123@gmail.com'])
                admin_email.attach_alternative(admin_email_html, "text/html")
                admin_email.send()
            except Exception as e:
                logger.error(f"Failed to send email notification to admin: {e}")

            # Send email confirmation to user
            try:
                user_subject = 'Booking Confirmation'
                user_message = render_to_string('email/user_booking_notification.html', {
                    'username': booking_instance.username,
                    'useremail': booking_instance.useremail,
                    'telnumber': booking_instance.telnumber,
                    'destination': booking_instance.destination,
                    'howMany': booking_instance.howMany,
                    'arrivals': booking_instance.arrivals,
                    'bookmessage': booking_instance.bookmessage,
                })
                user_email_text = strip_tags(user_message)
                user_email_html = user_message
                user_email = EmailMultiAlternatives(user_subject, user_email_text, 'hirwacedric123@gmail.com', [booking_instance.useremail])
                user_email.attach_alternative(user_email_html, "text/html")
                user_email.send()
            except Exception as e:
                logger.error(f"Failed to send email confirmation to user: {e}")

            return render(request, 'book.html')  # Redirect to success page

    else:
        form = BookingForm()
    return render(request, 'index.html', {'form': form})
    