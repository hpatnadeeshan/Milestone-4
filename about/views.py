from django.shortcuts import render


def about(request):
    """A view to show about page"""
    return render(request, 'about/about_us.html')
