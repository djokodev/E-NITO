from django.urls import path
from store.views import home, product_detail

urlpatterns = [
   path("", home, name="home"),
   path("product/<str:slug>/", product_detail, name="product"),
]
