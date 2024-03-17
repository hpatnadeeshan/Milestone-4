from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('subscribers/', views.subscriber_list, name='subscriber_list'),
]
