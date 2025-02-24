from django.contrib import admin
from django.urls import path
from myapp import views  # Import views from myapp

app_name = "myapp"  # Helps with namespacing in templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'), 
    path('cart/', views.cart, name='cart'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('shop/', views.shop, name='shop'),  # ✅ Added shop
    path('blog/', views.blog, name='blog'), 
    path('checkout/', views.checkout, name='checkout'), # ✅ Added blog (Fix for NoReverseMatch)
]
