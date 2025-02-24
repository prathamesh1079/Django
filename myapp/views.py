from django.shortcuts import render, redirect
from .models import Contact, Cart, Services, About

def home(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if first_name and last_name and email and message:  # Ensure fields are not empty
            try:
                Contact.objects.create(first_name=first_name, last_name=last_name, email=email, message=message)
                return redirect('contact')  # Redirect to avoid duplicate submissions
            except Exception as e:
                print(f"Error saving contact: {e}")

    return render(request, 'contact.html')

def cart(request):
    if request.method == 'POST':
        user = request.POST.get('user', '').strip()
        product = request.POST.get('product', '').strip()
        quantity = request.POST.get('quantity', '').strip()
        price = request.POST.get('price', '').strip()

        if user and product and quantity and price:  # Ensure required fields are filled
            try:
                Cart.objects.create(user=user, product=product, quantity=quantity, price=price)
                return redirect('cart')  # Redirect to prevent duplicate form submission
            except Exception as e:
                print(f"Error saving cart entry: {e}")

    return render(request, 'cart.html')

def services(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        queries = request.POST.get('queries', '').strip()
        suggestions = request.POST.get('suggestions', '').strip()

        if name and queries:  # Ensure at least name and queries are provided
            try:
                Services.objects.create(name=name, queries=queries, suggestions=suggestions)
                return redirect('services')
            except Exception as e:
                print(f"Error saving service entry: {e}")

    return render(request, 'services.html')

def about(request):
    if request.method == 'POST':
        firm = request.POST.get('firm', '').strip()
        location = request.POST.get('location', '').strip()
        suggestions = request.POST.get('suggestions', '').strip()

        if firm and location:  # Ensure required fields are filled
            try:
                About.objects.create(firm=firm, location=location, suggestions=suggestions)
                return redirect('about')
            except Exception as e:
                print(f"Error saving about entry: {e}")

    return render(request, 'about.html')


def shop(request):
    return render(request, 'shop.html')  # Make sure shop.html exists in templates


def blog(request):
    return render(request, 'blog.html')  # Ensure blog.html exists in your templates


def checkout(request):
    return render(request, 'checkout.html')