from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('message-submit/', views.message_submit, name='message_submit'),
    path('gallery/', views.gallery, name='gallery'),
    path('team/', views.team, name='team'),
    path('book-consultation/', views.book_consultation, name='book_consultation'),
    path('confirmation/', views.confirmation, name='confirmation'),
]
