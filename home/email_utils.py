from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Subscriber
from .email_utils import send_confirmation_email

def subscribe_newsletter(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            # Check if the user is already subscribed
            subscriber = Subscriber.objects.get(email=email)
            # User is already subscribed, close the modal
            messages.info(request, 'You are already subscribed.')
        except ObjectDoesNotExist:
            # User is not subscribed, send confirmation email
            send_confirmation_email(email)
            messages.success(request, 'Thank you for subscribing!')
            Subscriber.objects.create(email=email)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
