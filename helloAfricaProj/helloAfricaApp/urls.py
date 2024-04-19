from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('safaris-description/', views.safarisDetails, name='safaris-details'),
    path('contact/send-message/', views.send_message, name='send-message'),
]