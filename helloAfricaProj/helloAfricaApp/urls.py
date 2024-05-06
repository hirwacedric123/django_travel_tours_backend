from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('safaris-description/', views.safarisDetails, name='safaris-details'),
    path('contact/send-message/', views.send_message, name='send-message'),
    path('book/', views.book_page, name='book-page'),
    path('contact_us/book', views.books, name='books'),
    path('terms-and-conditions/', views.terms_and_conditions, name='terms-and-conditions')
]