from django.shortcuts import render, redirect
from .forms import NewsletterSubscriptionForm
from .models import NewsletterSubscriber
from .email_utils import send_confirmation_email
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "home/index.html")


def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            NewsletterSubscriber.objects.create(email=email)
            send_confirmation_email(email)
            messages.success(request, "You have successfully subscribed to our newsletter!")
            # Render the same page with a success message
            form = NewsletterSubscriptionForm()  # Reset the form
            return render(request, "home/index.html")
    else:
        form = NewsletterSubscriptionForm()
    return render(request, "home/index.html")







