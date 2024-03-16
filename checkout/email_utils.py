from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

def send_confirmation_email(order):
    """Send a confirmation email to the user"""
    cust_email = order.email
    subject = render_to_string('checkout/confirmation_emails/confirmation_email_subject.txt', {'order': order})
    body = render_to_string('checkout/confirmation_emails/confirmation_email_body.txt', {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email]
    )
