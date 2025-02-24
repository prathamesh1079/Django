from django.contrib import admin
from .models import Contact, Cart, Services, About

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'message']  # Corrected field names

admin.site.register(Contact, ContactAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'price']  # Fixed attribute name

admin.site.register(Cart, CartAdmin)


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'queries', 'suggestions']  # Added 'queries'

admin.site.register(Services, ServicesAdmin)


class AboutAdmin(admin.ModelAdmin):
    list_display = ['firm', 'location', 'suggestions']  # Corrected field names

admin.site.register(About, AboutAdmin)
