from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('messages/', views.contact_messages_view,
         name='contact_messages_view'),
]
