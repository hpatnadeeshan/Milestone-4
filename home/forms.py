from django import forms


class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField()
