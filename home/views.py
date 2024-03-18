from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import NewsletterSubscriber
from .email_utils import send_confirmation_email


def index(request):
    return render(request, "home/index.html")


def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            NewsletterSubscriber.objects.get(email=email)
            messages.info(request, 'You are already subscribed.')
        except NewsletterSubscriber.DoesNotExist:
            NewsletterSubscriber.objects.create(email=email)
            send_confirmation_email(email)
            messages.success(request, 'Thank you for subscribing!')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def subscriber_list(request):
    subscribers = NewsletterSubscriber.objects.all()
    return render(request, 'home/subscriber_list.html',
                  {'subscribers': subscribers})
