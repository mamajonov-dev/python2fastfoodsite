from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('add-cart/<int:product_id>/', karkinkagaqoshish, name='karkinkagaqoshish'),

    path('karzinka/', karzinkanikorish, name='karzinkanikorish'),
    path('register/', registrview, name='register'),
    path('login/', loginview, name='login'),

    path('add-order/', addorder, name='addorder'),


    path('delete-cart-item/<int:cart_id>/', deletecartitem, name='deletecartitem')
]