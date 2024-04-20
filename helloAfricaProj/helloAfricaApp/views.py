from mailbox import Message
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import MessageForm
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives

# from .forms import BookingForm


from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render (request, 'contact.html')
def safarisDetails(request):
    return render (request, 'safaris-details.html')
def book_page(request):
    return render (request, 'book.html')







# View function for sending message
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message_instance = form.save()

            # Send email notification to admin
            subject_admin = 'New message from {}'.format(message_instance.name)
            admin_message_html = render_to_string('admin_notification_template.html', {
                'name': message_instance.name,
                'email': message_instance.email,
                'phone': message_instance.phone,
                'message': message_instance.message
            })
            admin_message_text = strip_tags(admin_message_html)
            admin_email = EmailMultiAlternatives(subject_admin, admin_message_text, 'hirwacedric123@gmail.com', ['hirwacedric123@gmail.com'])
            admin_email.attach_alternative(admin_message_html, "text/html")
            admin_email.send()

            # Send email confirmation to user
            subject_user = 'Message Confirmation'
            user_message_html = render_to_string('user_notification_template.html', {
                'name': message_instance.name,
                'email': message_instance.email,
                'phone': message_instance.phone,
                'message': message_instance.message
            })
            user_message_text = strip_tags(user_message_html)
            user_email = EmailMultiAlternatives(subject_user, user_message_text, 'hirwacedric123@gmail.com', [message_instance.email])
            user_email.attach_alternative(user_message_html, "text/html")
            user_email.send()

            return render(request, 'success.html')  # Redirect to success page

    else:
        form = MessageForm()

    return render(request, 'index.html', {'form': form})
