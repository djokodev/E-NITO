from django.urls import path
from store.views import home, product_detail, add_to_cart, cart, delete_cart

urlpatterns = [
   path("", home, name="home"),
   path("cart/", cart, name="cart"),
   path("cart/delete", delete_cart, name="delete_cart"),
   path("product/<str:slug>/", product_detail, name="product"),
   path("product/<str:slug>/add-to-cart/", add_to_cart, name="add_to_cart"),
]
