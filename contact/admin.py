# admin.py
from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'created_at']
    search_fields = ['name', 'email', 'message']
    list_filter = ['created_at']

admin.site.register(ContactMessage, ContactMessageAdmin)