from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from .models import ContactMessage

def contact(request):
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

    return render(request, 'contact.html', {'form': form})

