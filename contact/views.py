from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage
from django.contrib.auth.decorators import login_required

def contact(request):
    """A view to show contact form page"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, "Contact form submitted successfully")
            return redirect('home')
        else:
            messages.error(
                request,
                "Update failed. Please ensure the form is valid.",
            )
    else:
        form = ContactForm()

    return render(request, 'contact/contact_us.html', {'form': form})

@login_required
def contact_messages_view(request):
    """A view to show contact messages page"""
    contact_messages = ContactMessage.objects.all()
    return render(request, 'contact/contact_messages.html', {'contact_messages': contact_messages})
